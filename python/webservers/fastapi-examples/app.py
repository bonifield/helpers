from fastapi import FastAPI
# use Pydantic to enforce typing and automate most error handling
from pydantic import BaseModel


# initialize the app
app = FastAPI()
# disable API documentation endpoints
'''
app = FastAPI(
	docs_url=None,
	openapi_url=None,
	redoc_url=None
)
'''


# FastAPI will use this Pydantic class as a schema to validate input data and return errors if the proper fields aren't provided
class UserName(BaseModel):
	# mandatory string argument
	first_name: str
	# the pipe-none statement makes this optional
	# not all users may have a last name
	last_name: str | None = None


# endpoint for the user to POST JSON data
@app.post("/posty")
async def posty(data: UserName):
	""" Returns a string based on a JSON submission. """
	# if the user doesn't send first_name, FastAPI will return a 4xx error
	# last_name is optional inside the UserName class
	if data.last_name:
		return f"Hello, {data.first_name} {data.last_name}!"
	else:
		return f"Hello, {data.first_name}!"


# obligatory hello world endpoint
@app.get("/helloworld")
async def hw():
	""" Hello, world! """
	# return JSON
	return {"message": "Hello, World!"}
