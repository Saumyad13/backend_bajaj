from flask import Flask, request, jsonify
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get('data', [])
        file_b64 = request.json.get('file_b64', None)
        user_info = {
            "user_id": "john_doe_17091999",  # Replace with actual logic if needed
            "email": "john@xyz.com",
            "roll_number": "ABCD123"
        }

        # Extract numbers and alphabets
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]

        # Find highest lowercase alphabet
        lowercase_alphabets = [ch for ch in alphabets if ch.islower()]
        highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None

        # File validation (if file_b64 exists)
        file_valid = False
        file_mime_type = None
        file_size_kb = None
        if file_b64:
            try:
                decoded_file = base64.b64decode(file_b64)
                file_size_kb = len(decoded_file) / 1024  # File size in KB
                file_valid = True
                file_mime_type = "image/png"  # Example, modify based on real logic
            except Exception as e:
                file_valid = False

        response = {
            "is_success": True,
            **user_info,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else [],
            "file_valid": file_valid,
            "file_mime_type": file_mime_type,
            "file_size_kb": file_size_kb
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400


@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200


if __name__ == '__main__':
    app.run(debug=True)
