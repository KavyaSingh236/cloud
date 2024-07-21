from flask import Flask, request, jsonify
import time
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/data', methods=['POST'])
def process_data():
    start_time = time.time()
    data = request.json
    logging.info(f"Received data: {data}")  # Log the incoming data
    patient = data['patient']
    heart_rate = data['heart_rate']
    blood_pressure = data['blood_pressure']
    blood_oxygen = data['blood_oxygen']
    # Simulate longer processing time
    time.sleep(1)
    end_time = time.time()
    processing_time = end_time - start_time
    return jsonify({"status": "success", "processing_time": processing_time})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
