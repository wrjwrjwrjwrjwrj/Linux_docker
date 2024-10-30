from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/display_results', methods=['GET'])
def display_results():
    results_response = requests.get('http://calculation:5001/calculate')
    results = results_response.json()
    print(results)  # 可以保存或进一步处理结果
    return jsonify({"message": "Results displayed successfully!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)