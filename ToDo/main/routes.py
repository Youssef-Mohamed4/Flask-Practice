from flask import render_template, Blueprint

main = Blueprint("main", __name__)

@main.route('/')
@main.route('/Home')
def home():
    return render_template('index.html',title='Home')