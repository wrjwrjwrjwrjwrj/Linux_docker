from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

@app.route('/load_data', methods=['GET'])
def load_data():
    # 获取当前文件的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建数据文件的绝对路径
    data_file_path = os.path.join(current_dir, 'Grade Table.csv')
    data = pd.read_csv(data_file_path)
    print(data.head())
    return jsonify(data.to_dict())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)