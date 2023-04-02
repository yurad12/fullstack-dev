from flask import Flask, request, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET','POST','PUT','DELETE'])
def test():
    if request.method == 'POST':
        data = request.get_json() # dictionary type
        print(data)
        print(data['email'])
    if request.method == 'GET':
        print('GET')
        user = request.args.get('email')
        print(user)
    if request.method == 'PUT':
        print('PUT')
        user = request.args.get('email')
        print(user)
    if request.method == 'DELETE':
        print('DELETE')
        user = request.args.get('email')
        print(user)

    # return jsonify( {'status':'success'} )
    return make_response(jsonify({'status':True}), 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8082')