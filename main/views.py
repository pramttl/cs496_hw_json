from django.shortcuts import render_to_response
from django.http import HttpResponse
import json
import requests

from .models import *
import random

from django.views.decorators.csrf import csrf_exempt


def index(request):
    """
    The home page which gives the user a random JSON reading problem
    from the database.
    """
    questions = JsonQuestion.objects.all()
    if questions:
        question = random.choice(questions)
        context_data = { "question": question}
        return render_to_response('question.html', context_data)
    else:
        return HttpResponse("Sorry no questions yet")


@csrf_exempt
def check(request):
    """
    Checks whether the output json of the endpoint provided by the student
    matches with the expected output.
    """
    qid = request.POST.get("qid")
    webendpoint = request.POST.get("webendpoint")

    question = JsonQuestion.objects.get(id=qid)

    print question.input_json

    # Load+Dump once just to make JSON is clean
    input_dict = json.loads(question.input_json)
    data = json.dumps(input_dict)

    # Get corresponding output from the database
    expected_output = json.loads(question.output_json)

    response = requests.post(webendpoint, params={}, data=data)

    try:
        user_output = response.json()
    except:
        error = "1. Invalid Json format returned by your endpoint"
        return render_to_response('check.html', {error: error, user_output: "N/A"})

    print "============="
    print type(expected_output)

    # If the expected output is list style json
    if type(expected_output) == list:
        if type(user_output) == list:

            if set(expected_output) == set(user_output):
                if expected_output == user_output:
                    error = """There is no error. Congratulations you successfully solved this question
                    Unless you manually printed the output"""
                    return render_to_response('check.html', {error: error, user_output: json.dumps(user_output)})
                else:
                    error = "3. The order of elements in your output does not match with our test case. Please check."
                    return render_to_response('check.html', {error: error, user_output: json.dumps(user_output)})                    

        else:
            error = "2. Something seems to be wrong with your output JSON type: {} instead of []"
            return render_to_response('check.html', {error: error, user_output: json.dumps(user_output)})

    # If the expected output is a dictionary style json
    elif type(expected_output) == dict:
        if type(user_output) == dict:
            if expected_output == user_output:
                    error = """There is no error. Congratulations you successfully solved this question
                    Unless you manually printed the output"""
                    return render_to_response('check.html', {error: error, user_output: json.dumps(user_output)})
        else:
            return HttpResponse("2. Something seems to be wrong with your output JSON type: [] instead of []")
    else:
        return HttpResponse("Your endpoint output pwned the applicaiton! :( Contact TA or instructor")