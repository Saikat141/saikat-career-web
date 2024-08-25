from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

if __name__ == "__main__":
    app.run("0.0.0.0",debug=True)