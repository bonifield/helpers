#!/usr/bin/env python3


from flask import Flask, request, jsonify


# set custom Server response header
SERVER_NAME = 'My Custom Flask Application v0.1.0'
class LocalFlask(Flask):
	def process_response(self, response):
		""" Include these headers in the HTTP response. """
		response.headers['Server'] = SERVER_NAME
		return response
app = LocalFlask(__name__)
#app = Flask(__name__)
# secret application key
app.secret_key = "test secret key, please change in production"


# POST endpoint
@app.route('/posty', methods=['POST'])
def posty():
	""" Accepts JSON via POST and returns a string. """
	if request.is_json:
		# convert to dict
		data = request.get_json()
		out = ["Hello,"]
		if data.get("first_name"):
			out.append(str(data["first_name"]))
		if data.get("last_name"):
			out.append(str(data["last_name"]))
		return " ".join(out) + "!"
	# if the user specifies "Content-Type: application/json" but
	# doesn't send JSON, they will receive a 400 instead of the
	# string in th else statement
	else:
		return "No JSON sent to server!"


# obligatory hello world GET endpoint that returns JSON
@app.route('/helloworld')
def hw():
	""" Hello, world! """
	# jsonify sets response headers, converts objects to JSON strings,
	# and pretty-prints the JSON
	return jsonify({"message": "Hello, world!"})


# custom error 400 handler
@app.errorhandler(400)
def bad_request(e):
	""" Custom HTTP 400 response handler. """
	return("oops, four hundred")


# create application on localhost:8080 with self-signed certificate
if __name__ == "__main__":
	app.run(host="127.0.0.1", port=8080, debug=True, ssl_context="adhoc")
