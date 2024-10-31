from flask import Flask

app = Flask(__name__)

@app.route('/healthz', methods=['GET'])
def hello_get():
    return '', 200

@app.route('/healthz', methods=['POST'])
def hello_post():
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
