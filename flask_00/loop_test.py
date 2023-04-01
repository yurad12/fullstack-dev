from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello_loop')
def hello_name():
    fruits = ['apple','banana','melon']
    return render_template('loop.html', fruits=fruits) # html파일에서 사용할 변수 이름으로

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')