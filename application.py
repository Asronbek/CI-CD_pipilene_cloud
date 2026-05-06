from flask import Flask, jsonify

application = Flask(__name__)

@application.route('/')
def hello():
    return '<h1>Hello from CI/CD Pipeline 🚀</h1>', 200

@application.route('/health')
def health():
    return jsonify(status='ok'), 200

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)