from flask import Flask, jsonify, request, session

app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello, World!'

@app.route('/api/hello')
def hello():
  return '''テキストボックスの入力を受け取って、
  「○○さんこんにちわ」と表示してみましょう。'''

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8081)
