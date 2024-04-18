from flask import Flask

 # Initializes the application 
app = Flask(__name__)

# Adds route
@app.route("/")
def home():
    return "home page"

# Runs the app
if __name__ == '__main__':
 app.run(debug=True)
