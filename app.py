from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
@app.route("/Home",methods=['GET','POST'])
def home():
    return render_template('index.html', title='Home', style='home.css')

@app.route("/About")
def about():
    return render_template('about.html', title='About',style='about.css')

if __name__== "__main__":
    app.run(debug=True , port=3000)