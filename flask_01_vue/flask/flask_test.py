from flask import Flask, request, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# http GET http://localhost:8082/test_vue

@app.route('/test_vue', methods=['GET'])
def test():
    return make_response(jsonify(success=True), 200)
    # return jsonify(success=True)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8082')