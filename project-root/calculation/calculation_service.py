from flask import Flask, request, jsonify
import requests
import pandas as pd

app = Flask(__name__)

@app.route('/calculate', methods=['GET'])
def calculate_totals():
    data_response = requests.get('http://data_loader:5000/load_data')
    data = pd.DataFrame(data_response.json())
    data['Total'] = data[['Chinese', 'Math', 'English', 'CloudComputing']].sum(axis=1)
    data['Max Diff'] = data[['Chinese', 'Math', 'English', 'CloudComputing']].max(axis=1) - data[['Chinese', 'Math', 'English', 'CloudComputing']].min(axis=1)
    return jsonify(data[['Name', 'Total', 'Max Diff']].to_dict())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)