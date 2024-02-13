import os  # Import the os module to interact with the operating system, e.g., reading environment variables.

from flask import Flask, render_template, request, jsonify  # Import necessary objects from Flask: Flask for the app, render_template to render HTML, request to handle requests, jsonify for JSON responses.
from flask_cors import CORS  # Import CORS to handle Cross-Origin Resource Sharing, allowing requests from different origins.
from dialogues.manager import DialogueManager  # Import DialogueManager, presumably to manage dialogues in your app.
from contracts.manager import ContractManager  # Import ContractManager, presumably to manage contract-related actions.
from utils.logger import logger  # Import a logger for logging messages.

app = Flask(__name__, static_folder='static')  # Create a Flask application instance. The static_folder parameter specifies the folder with static files.
CORS(app)  # Apply CORS settings to the Flask app to allow cross-origin requests.

dialogue_manager = DialogueManager()  # Instantiate the DialogueManager.
contract_manager = ContractManager()  # Instantiate the ContractManager.


@app.route('/')  # Define a route for the root URL ("/").
def index():
    return render_template('index.html')  # Render and return the 'index.html' template when the root URL is accessed.


@app.route('/process_input', methods=['POST'])  # Define a route for processing input with URL "/process_input", allowing only POST requests.
def process_input():
    try:
        data = request.get_json()  # Try to parse the incoming request data as JSON.
        user_input = data.get('user_input', '')  # Extract the 'user_input' field from the JSON data, defaulting to an empty string if not found.

        response, action = dialogue_manager.process_input(user_input)  # Process the user input using DialogueManager and get a response and action.

        if action == "generate_contract":  # Check if the action indicates a contract should be generated.
            contract_details = data.get('details', {})  # Extract contract details from the data, defaulting to an empty dictionary.
            contract_response = contract_manager.generate_contract(contract_details)  # Use ContractManager to generate a contract with the provided details.
            response = f"Contract generated: {contract_response}"  # Update the response to include the contract generation result.

        return jsonify({'response': response})  # Return the response as a JSON object.
    except Exception as e:
        logger.error(f"Error processing request: {e}")  # Log any exceptions that occur during request processing.
        return jsonify({'error': 'Error processing your request'}), 500  # Return a JSON response indicating an error, with a 500 Internal Server Error status.


if __name__ == '__main__':  # Check if this script is executed as the main program.
    debug_mode = os.getenv('FLASK_DEBUG', 'False') == 'True'  # Read the FLASK_DEBUG environment variable to determine if debug mode should be enabled.
    app.run(host='0.0.0.0', port=5002, debug=debug_mode)  # Run the Flask application with the specified host, port, and debug mode settings.
