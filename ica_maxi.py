from bs4 import BeautifulSoup
import requests

def update_maxi_data():

  ica_maxi_mince = requests.get('https://handlaprivatkund.ica.se/stores/1004219/search?q=blandf%C3%A4rs&sortBy=pricePerDescending')
  soup_maxi_mince = BeautifulSoup(ica_maxi_mince.text, 'lxml')
  mince_maxi_name = soup_maxi_mince.find('h3', class_ = 'text__Text-sc-6l1yjp-0 iWlLMY').text
  mince_maxi_price = soup_maxi_mince.find('div', class_ = 'base__PriceWrapper-sc-1mnb0pd-28 dDLLyP').text

  ica_maxi_cheese = requests.get('https://handlaprivatkund.ica.se/stores/1004219/search?q=ost&sortBy=pricePerDescending')
  soup_maxi_cheese = BeautifulSoup(ica_maxi_cheese.text, 'lxml')
  cheese_maxi_name = soup_maxi_cheese.find('h3', class_ = 'text__Text-sc-6l1yjp-0 iWlLMY').text
  cheese_maxi_price = soup_maxi_cheese.find('div', class_ = 'base__PriceWrapper-sc-1mnb0pd-28 dDLLyP').text

# Reading existing HTML file
  file_path = 'templates/index.html'
  with open(file_path, 'r') as file:
   html_content = file.read()

  #Parseing the HTML content
   soup = BeautifulSoup(html_content,'lxml')

   #Locates the specific cell by id
   maxi_cell1_id = 'maxi_mince_name'
   maxi_cell2_id = 'maxi_mince_price'
   maxi_cell3_id = 'maxi_cheese_name'
   maxi_cell4_id = 'maxi_cheese_price'
   maxi_cell5_id = 'maxi_fish_name'
   maxi_cell6_id = 'maxi_fish_price'
   maxi_cell7_id = 'maxi_potatoe_name'
   maxi_cell8_id = 'maxi_potatoe_price'
   maxi_cell9_id = 'maxi_chicken_name'
   maxi_cell10_id = 'maxi_chicken_price'

   maxi_cell1= soup.find('td', id=maxi_cell1_id)
   maxi_cell2= soup.find('td', id=maxi_cell2_id)
   maxi_cell3= soup.find('td', id=maxi_cell1_id)
   maxi_cell4= soup.find('td', id=maxi_cell2_id)
   maxi_cell5= soup.find('td', id=maxi_cell1_id)
   maxi_cell6= soup.find('td', id=maxi_cell2_id)
   maxi_cell7= soup.find('td', id=maxi_cell1_id)
   maxi_cell8= soup.find('td', id=maxi_cell2_id)
   maxi_cell9= soup.find('td', id=maxi_cell1_id)
   maxi_cell10= soup.find('td', id=maxi_cell2_id)
  
   #Update the content of the mince name cell 
   if maxi_cell1:
    maxi_cell1.string = mince_maxi_name
   else:
     print(f"No cell found")

   #Update the content of the mince price cell

  if maxi_cell2:
     maxi_cell2.string = mince_maxi_price
  else:
     print(f"No cell found")

  with open(file_path, 'w') as file:
     file.write(str(soup))

  print(f"Mince name has been added")