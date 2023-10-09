from flask import Flask, request, jsonify
import socket
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/ping')  # 设置路由为 /ping
def get_server_info():
    # 获取服务器当前时间
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # 获取服务器IP地址
    ip_address = socket.gethostbyname(socket.gethostname())

    # 构建响应数据
    response_data = {
        'time': current_time,
        'ip': ip_address
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
