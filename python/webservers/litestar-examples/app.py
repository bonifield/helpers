# import Litestar class and method decorators
from litestar import Litestar, get, post
# use Pydantic to enforce typing and automate most error handling
from pydantic import BaseModel


# Litestar will use this Pydantic class as a schema to validate input data and return errors if the proper fields aren't provided
class UserName(BaseModel):
	# mandatory string argument
	first_name: str
	# the pipe-none statement makes this optional
	# not all users may have a last name
	last_name: str | None = None


# endpoint for the user to POST JSON data
@post("/posty")
async def posty(data: UserName) -> str:
	""" Returns a string based on a JSON submission. """
	# if the user doesn't send first_name, Litestar will return a 400 error
	# last_name is optional inside the UserName class
	if data.last_name:
		return f"Hello {data.first_name} {data.last_name}!"
	else:
		return f"Hello {data.first_name}!"


# obligatory hello world endpoint
@get("/helloworld")
async def hw() -> dict:
	""" Hello, world! """
	# return JSON
	return {"message": "Hello, World!"}


# create application and pass route handlers
app = Litestar(route_handlers=[hw, posty])
