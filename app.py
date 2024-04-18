from flask import Flask, render_template

 # Initializes the application 
app = Flask(__name__)

# Adds route
@app.route("/")
def home():
    return render_template("index.html")

# Runs the app
if __name__ == '__main__':
 app.run(debug=True)
