from flask import Flask, render_template

app = Flask(__name__, static_url_path='', static_folder="build", template_folder='build')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

