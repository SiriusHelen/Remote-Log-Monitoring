from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("nav.html")

@app.route('/chart')
def bye():
    return render_template("chart.html")
if __name__ == '__main__':
  app.run()


@app.route('/hello')
def bye():
    return render_template("hello.html")
if __name__ == '__main__':
  app.run()

