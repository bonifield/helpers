# Litestar Examples

# Documentation
[Website](https://litestar.dev/) [GitHub](https://github.com/litestar-org/litestar)

## Installation
```
uv init
uv add litestar pydantic uvicorn
```
**Rename `main.py` to `app.py`**

## Running `app.py`
`uv run litestar run --host 127.0.0.1 --port 8080`

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
curl -s -X POST 127.0.0.1:8080/posty -H "Content-Type: application/json" -d '{"first_name":"bob", "last_name":"smith"}'
# response
Hello, bob smith!
```

## Generating an Error
omit the required `first_name` attribute
```
curl -s -X POST 127.0.0.1:8080/posty -H "Content-Type: application/json" -d '{"last_name":"smith"}' | jq
# response
{
  "status_code": 400,
  "detail": "Validation failed for POST /posty",
  "extra": [
    {
      "message": "Field required",
      "key": "first_name"
    }
  ]
}
```
