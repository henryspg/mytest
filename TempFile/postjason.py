# https://www.youtube.com/watch?v=VzBtoA_8qm4

from flask import request






@app.route("/json", methods=["POST"])
def json_example():

    # Validate the request body contains JSON
    if request.is_json:

        # Parse the JSON into a Python dictionary
        req = request.get_json()

        # Print the dictionary
        print(req)

        # Return a string along with an HTTP status code
        return "JSON received!", 200

    else:

        # The request body wasn't JSON so return a 400 HTTP status code
        return "Request was not JSON", 400

