# Import the Flask class, as well as jsonify and request from Flask
from flask import Flask, jsonify, request

# Create a Flask web application instance
app = Flask(__name__) 

# Define a route for the root URL ('/'). This is the main page of the API.
# This route handles both GET and POST requests.
@app.route('/', methods=['GET', 'POST'])
def index():
    # Check if the request method is GET
    if request.method == 'GET':
        # If it is a GET request, create a response data
        data = "Amen Brother :)"
        # Return a JSON response
        return jsonify({'Greetings fuckers': data})

# Define a route that takes an integer parameter in the URL
# For example, if the URL is '/5', it will return the cube of 5
@app.route('/<int:num>', methods=['GET'])
def cube(num):
    # Calculate the cube of the provided number
    result = num ** 3
    # Return a JSON response with the result
    return jsonify({f'cube number of {num}': result})

# Run the application if this script is the main script
if __name__ == "__main__":
    # Start the Flask development server with debugging enabled
    app.run(debug=True)
