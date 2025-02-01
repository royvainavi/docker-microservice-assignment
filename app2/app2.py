from flask import Flask, request, jsonify
import os
import csv

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    filename = data['file']
    product = data['product']
    
    file_path = os.path.join('/data', filename)
    
    if not os.path.isfile(file_path):
        return jsonify({"file": filename, "error": "File not found."}), 400
    
    try:
        total = 0
        with open(file_path, 'r') as f:
            # Check if the file is empty
            if os.stat(file_path).st_size == 0:
                return jsonify({"file": filename, "error": "Input file not in CSV format."}), 400
            
            # Read the first line to check for headers
            first_line = f.readline().strip()
            if not first_line or ',' not in first_line:
                return jsonify({"file": filename, "error": "Input file not in CSV format."}), 400
            
            # Reset file pointer and parse CSV
            f.seek(0)
            reader = csv.DictReader(f)
            if 'product' not in reader.fieldnames or 'amount' not in reader.fieldnames:
                return jsonify({"file": filename, "error": "Input file not in CSV format."}), 400
            
            # Calculate sum
            for row in reader:
                if row['product'] == product:
                    try:
                        total += int(row['amount'])
                    except ValueError:
                        return jsonify({"file": filename, "error": "Input file not in CSV format."}), 400
        return jsonify({"file": filename, "sum": total})
    except (csv.Error, KeyError, ValueError):
        return jsonify({"file": filename, "error": "Input file not in CSV format."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
