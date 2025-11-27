from datetime import datetime, timezone
from flask import Flask


app = Flask(__name__)


@app.route("/")
def get_utc_timestamp():
	"""Returns an ISO8601 timestamp and a newline character."""
	return datetime.now(timezone.utc).isoformat()+"\n"


# module loads the app directly, so set environment variables
# since the if __main__ block doesn't run
#     export FLASK_RUN_HOST=0.0.0.0
#     uv run flask --app app.py run
# or dev only, use the __main__ block: python app.py
if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=5000)
