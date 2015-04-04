### Description

Students enter an endpoint of their web application which is designed to take a JSON object as input via POST.

Their endpoint should read a JSON input and output some reformatted JSON contaning the relevant information which the question asks.

The administrator in the database can create an input JSON and an output JSON and a question. An administrator should be able to add multiple `JsonQuestion` objects.

`JsonQuestion` has 3 fields of Text type.

A. Input JSON
B. Question
C. Output JSON

Only A & B are shown to the students. 

### Rules

1. The root endpoint the student submits should be able to receive a POST request with raw json data.  The current app, lets call it `ShootMeJson` will post the json to the endpoint submitted by the user.

2. The page must return raw JSON as the question asks them to.

3. If the output JSON is correct (as per what the question asks) then the student is shown CORRECT else the student is shown WRONG with the expected JSON output. 

(The output is compared with an internal associative array. The order of keys in an object does not matter, but the order of elements in the lit does matter.)