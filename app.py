from flask import Flask, request, jsonify
from flask_cors import CORS
import angrybot
app = Flask(__name__)

CORS(app)


@app.route('/api/bot', methods= ['GET', 'POST'])
def index():
    user_input= request.args.get("user_input")
    print(user_input)
    res = str(angrybot.chatresponse(user_input))
    return jsonify({'message': res})

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 