from flask import Flask, render_template, request
import sql # imports sql.py 

app = Flask(__name__, static_url_path='', static_folder="build", template_folder='build')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/menu', methods=['GET', 'POST']) #route for menu in database
def menu(): 
    if request.method == 'GET': #handles get requests
        return {'response': sql.view()} #returns table in JSON format
    elif request.method == 'POST': #handles adding requests
        data = request.json
        sql.add( data['id'], data['name'], data['img_url'], data['description'], data['price'])
        return {'response': sql.view()}

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
