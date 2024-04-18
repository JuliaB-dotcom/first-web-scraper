from flask import Flask

 #initializes the application 
app = Flask(__name__)

#runs the app
if __name__ == '__main__':
 app.run(debug=True)
