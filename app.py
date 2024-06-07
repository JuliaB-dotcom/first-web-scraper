from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

 # Initializes the application 
app = Flask(__name__)

# Adds route
@app.route('/')
def home():
    try:
        ica_maxi_mince = requests.get('https://handlaprivatkund.ica.se/stores/1004219/search?q=blandf%C3%A4rs&sortBy=pricePerDescending')
        soup_mince = BeautifulSoup(ica_maxi_mince.text, 'lxml')
        mince_name = soup_mince.find('h3', class_ = 'text__Text-sc-6l1yjp-0 iWlLMY').text
        mince_price = soup_mince.find('div', class_ = 'base__Price-sc-1mnb0pd-29 sc-dJjZJu gsTqdV gShugV').text
        mince_info =  mince_name + '' + mince_price
    
    except requests.RequestException as e:
    # Handle request exceptions
        mince_price = f"Error fetching data: {e}"
    
    except Exception as e:
    # Handle all other exceptions
        mince_price= f"An error occurred: {e}"

    return render_template("index.html", mince_price=mince_price)

# Runs the app
if __name__ == '__main__':
 app.run(debug=True)
