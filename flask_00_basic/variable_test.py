from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
    # name1은 입력값 받고, name2는 고정값
    return render_template('variable.html', name1=user, name2=20)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')