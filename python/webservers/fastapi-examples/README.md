# FastAPI Examples

# Documentation
[Website](https://fastapi.tiangolo.com/) [GitHub](https://github.com/fastapi/fastapi)

## Installation
```
uv init
uv add fastapi uvicorn
```
**Rename `main.py` to `app.py`**

## Running `app.py`
with `uv`
```
uv run uvicorn app:app --host 127.0.0.1 --port 8080 --reload
```

with `uvicorn` outside a virtual environment
```
uvicorn app:app --host 127.0.0.1 --port 8080 --reload
```

## Querying the `GET` API
```
curl -s 127.0.0.1:8080/helloworld | jq
# response
{
  "message": "Hello, World!"
}
```

## Querying the `POST` API
```
curl -s -X POST 127.0.0.1:8080/posty -H "Content-Type: application/json" -d '{"first_name": "bob", "last_name":"smith"}'
# response
"Hello, bob smith!"
```

## Generating an Error
omit the required `first_name` parameter
```
curl -s -X POST 127.0.0.1:8080/posty -H "Content-Type: application/json" -d '{"last_name":"smith"}' | jq
# response
{
  "detail": [
    {
      "type": "missing",
      "loc": [
        "body",
        "first_name"
      ],
      "msg": "Field required",
      "input": {
        "last_name": "smith"
      }
    }
  ]
}
```

POST a string instead of JSON
```
curl -s -X POST 127.0.0.1:8080/posty -H "Content-Type: application/json" -d 'AAAA' | jq
# response
{
  "detail": [
    {
      "type": "json_invalid",
      "loc": [
        "body",
        0
      ],
      "msg": "JSON decode error",
      "input": {},
      "ctx": {
        "error": "Expecting value"
      }
    }
  ]
}
```

## Access API Documentation Endpoints
in the browser
```
127.0.0.1:8080/docs
127.0.0.1:8080/openapi.json
127.0.0.1:8080/redoc
```

## Disable API Documentation Endpoints
```
app = FastAPI(
	docs_url=None,
	openapi_url=None,
	redoc_url=None
)
```
