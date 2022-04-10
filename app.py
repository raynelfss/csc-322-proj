from flask import Flask, render_template, request
from api.index import apiBlueprint #imports apiBlueprint from ./api/index.py

app = Flask(__name__, static_url_path='', static_folder="build", template_folder='build')

@app.route('/')
def index(): return render_template("index.html")

@app.route('/menu')
def menupage(): return render_template("menu.html")

@app.route('/menu/edit')
def menueditpage(): return render_template("menu-staff.html")

# all api calls /api
app.register_blueprint(apiBlueprint)

if __name__ == '__main__': app.run(debug=True, use_reloader=False)
