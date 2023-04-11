from flask import Flask
import requests, logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

app.debug = False
if not app.debug:
    file_handler = RotatingFileHandler('yujeong_server.log', maxBytes=2000, backupCount=10)
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return '<h1>요청하신 페이지가 존재하지 않습니다. 해당 오류가 지속된다면, 고객센터로 연락바랍니다.</h1>',404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=False) # debug=True : Debug mode가 on/off