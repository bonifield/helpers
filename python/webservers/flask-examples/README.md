# Flask Examples

# Documentation
[Website](https://flask.palletsprojects.com/en/stable/) [GitHub](https://github.com/pallets/flask)

## Installation
```
uv init
uv add flask cryptography
```
**Rename `main.py` to `app.py`**

## Running `app.py`
with `uv`
```
uv run app.py
```

with `python3` which invokes the if name is main block
```
python3 app.py
````

using the `flask` command which uses port 5000
```
flask --app app.py run
```

## Querying the `GET` API
```
curl -sk https://127.0.0.1:8080/helloworld | jq
# response
{
  "message": "Hello, World!"
}
```

## Querying the `POST` API
```
curl -sk -X POST https://127.0.0.1:8080/posty -H "Content-Type: application/json" -d '{"first_name":"bob", "last_name":"smith"}'
# response
Hello, bob smith!
```

## Generating an Error
POST a string instead of JSON
```
curl -sk -X POST https://127.0.0.1:8080/posty -H "Content-Type: application/json" -d 'AAAA'
# response
<!doctype html>
<html lang=en>
<title>400 Bad Request</title>
<h1>Bad Request</h1>
<p>Failed to decode JSON object: Expecting value: line 1 column 1 (char 0)</p>
```

## Generating an Error with Custom Handler
```
curl -sk -X POST https://127.0.0.1:8080/posty -H "Content-Type: application/json" -d 'AAAA'
# response
oops, four hundred
```
