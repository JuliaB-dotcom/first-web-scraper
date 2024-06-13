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
        ica_maxi_cheese = requests.get('https://handlaprivatkund.ica.se/stores/1004219/search?q=ost&sortBy=pricePerDescending')
        soup_maxi_cheese = BeautifulSoup(ica_maxi_cheese.text, 'lxml')
        cheese_maxi_name = soup_maxi_cheese.find('h3', class_ = 'text__Text-sc-6l1yjp-0 iWlLMY').text
        cheese_maxi_price = soup_maxi_cheese.find('div', class_ = 'base__PriceWrapper-sc-1mnb0pd-28 dDLLyP').text

        ica_maxi_fish = requests.get('https://handlaprivatkund.ica.se/stores/1004219/search?q=fisk&sortBy=pricePerDescending')
        soup_maxi_fish = BeautifulSoup(ica_maxi_fish.text, 'lxml')
        fish_maxi_name = soup_maxi_fish.find('h3', class_ = 'text__Text-sc-6l1yjp-0 iWlLMY').text
        fish_maxi_price = soup_maxi_fish.find('div', class_ = 'base__PriceWrapper-sc-1mnb0pd-28 dDLLyP').text

        ica_maxi_potato = requests.get('https://handlaprivatkund.ica.se/stores/1004219/search?q=Fast%20Potatis&sortBy=pricePerDescending')
        soup_maxi_potato = BeautifulSoup(ica_maxi_potato.text, 'lxml')
        potato_maxi_name = soup_maxi_potato.find('h3', class_ = 'text__Text-sc-6l1yjp-0 iWlLMY').text
        potato_maxi_price = soup_maxi_potato.find('div', class_ = 'base__PriceWrapper-sc-1mnb0pd-28 dDLLyP').text
    


        return render_template("index.html", cheese_maxi_name=cheese_maxi_name,
                                cheese_maxi_price=cheese_maxi_price, fish_maxi_name=fish_maxi_name, fish_maxi_price=fish_maxi_price,
                                  potato_maxi_name=potato_maxi_name, potato_maxi_price=potato_maxi_price)

# Runs the app
if __name__ == '__main__':
 app.run(debug=True)
