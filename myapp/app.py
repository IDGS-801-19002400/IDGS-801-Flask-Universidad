from flask import Flask, render_template, request, redirect, url_for
from maestros.routes import maestros
from alumnos.routes import alumnos

app = Flask(__name__)
app.config['DEBUG'] = True

app.register_blueprint(maestros)
app.register_blueprint(alumnos)

@app.route('/')
def index():
    return 'Index'

if __name__ == '__main__':
    app.run()
