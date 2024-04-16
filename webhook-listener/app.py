from flask import Flask, jsonify, request
import os
import sys
import logging
import yaml

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True

logger = logging.getLogger('gunicorn.error')

def check_env_variable(var_name):
    if var_name not in os.environ:
        logger.critical(f"Error: Environment variable {var_name} is not set.")
        raise RuntimeError(f"Error: Environment variable {var_name} is not set.")
    return os.environ[var_name]

# Load
SERVER_API_KEY = check_env_variable('SERVER_API_KEY')
SERVER_PORT = int(check_env_variable('SERVER_PORT'))

@app.route('/')
@app.route('/health')
def health_check():
    # Return service health information
    return jsonify(status='healthy', message='Service is up and running!')

@app.route('/webhook', methods=['GET'])
def webhook_get():
    # Return service health information
    return jsonify(status='healthy', message='Please POST oura requests to this endpoint!')

@app.route('/webhook', methods=['POST'])
def webhook_post():
    if request.is_json:
        try:
            # Parse JSON to dictionary
            request_data = request.get_json()
            
            # Convert dictionary to YAML
            yaml_data = yaml.dump(request_data)
            
            # Log the YAML string
            logger.info("\n================[WEBHOOK]================\n%s=========================================", yaml_data)
            
            # Respond back to the client
            return jsonify({"message": "Payload received and logged"}), 200
        except Exception as e:
            logger.error("Error processing JSON: %s", str(e))
            return jsonify({"error": "Error processing JSON"}), 500
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=SERVER_PORT)
