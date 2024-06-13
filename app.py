from flask import Flask, render_template
from bs4 import BeautifulSoup
from ica_maxi import update_maxi_data
import requests

 # Initializes the application 
app = Flask(__name__)

# Adds route
@app.route('/')
def home():
    
        update_maxi_data()
        
        return render_template("index.html")

# Runs the app
if __name__ == '__main__':
 app.run(debug=True)
