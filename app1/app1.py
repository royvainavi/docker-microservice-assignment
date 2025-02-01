from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    
    if 'file' not in data or data['file'] is None:
        return jsonify({"file": None, "error": "Invalid JSON input."}), 400
    
    filename = data['file']
    product = data.get('product', '')
    
    file_path = os.path.join('/data', filename)
    if not os.path.isfile(file_path):
        return jsonify({"file": filename, "error": "File not found."}), 400
    
    try:
        response = requests.post(
            'http://app2:5000/process',
            json={"file": filename, "product": product}
        )
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"file": filename, "error": "Internal server error."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
