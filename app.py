from flask import Flask,render_template
from forms import RegisterForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']="fadffffffffff sfgggg"

@app.route('/')
@app.route("/Home",methods=['GET','POST'])
def home():
    return render_template('index.html', title='Home', style='home.css')


@app.route("/About")
def about():
    return render_template('about.html', title='About',style='about.css')

@app.route("/Register", methods=['GET','POST'])
def register():
    obj = RegisterForm()
    if obj.validate_on_submit():
        pass

    return render_template("register.html",title="Register",form=obj)


@app.route("/Login", methods=['GET','POST'])
def login():
    obj=LoginForm()
    if obj.validate_on_submit():
        pass

    return render_template("login.html",title="Login",form=obj)

if __name__== "__main__":
    app.run(debug=True , port=3000)