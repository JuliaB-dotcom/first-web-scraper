from bs4 import BeautifulSoup
import requests

def update_maxi_data():

  ica_maxi_mince = requests.get('https://handlaprivatkund.ica.se/stores/1004219/search?q=blandf%C3%A4rs&sortBy=favorite')
  soup_maxi_mince = BeautifulSoup(ica_maxi_mince.text, 'lxml')
  mince_maxi_name = soup_maxi_mince.find('h3', class_ = '_text_f6lbl_1 _text--m_f6lbl_23').text
  mince_maxi_price = soup_maxi_mince.find('span', class_ = '_text_f6lbl_1 _text--m_f6lbl_23 utils__PriceText-sc-1fkdssq-0 ifeOmJ').text

  ica_maxi_cheese = requests.get('https://handlaprivatkund.ica.se/stores/1004219/search?q=ost&sortBy=favorite')
  soup_maxi_cheese = BeautifulSoup(ica_maxi_cheese.text, 'lxml')
  cheese_maxi_name = soup_maxi_cheese.find('h3', class_ = '_text_f6lbl_1 _text--m_f6lbl_23').text
  cheese_maxi_price = soup_maxi_cheese.find('span', class_ = '_text_f6lbl_1 _text--m_f6lbl_23 utils__PriceText-sc-1fkdssq-0 ifeOmJ').text

  ica_maxi_fish = requests.get('https://handlaprivatkund.ica.se/stores/1004219/search?q=fisk&sortBy=favorite')
  soup_maxi_fish = BeautifulSoup(ica_maxi_fish.text, 'lxml')
  fish_maxi_name = soup_maxi_fish.find('h3', class_ = '_text_f6lbl_1 _text--m_f6lbl_23').text
  fish_maxi_price = soup_maxi_fish.find('span', class_ = '_text_f6lbl_1 _text--m_f6lbl_23 utils__PriceText-sc-1fkdssq-0 ifeOmJ').text

  ica_maxi_potato = requests.get('https://handlaprivatkund.ica.se/stores/1004219/search?q=Fast%20Potatis&sortBy=favorite')
  soup_maxi_potato = BeautifulSoup(ica_maxi_potato.text, 'lxml')
  potato_maxi_name = soup_maxi_potato.find('h3', class_ = '_text_f6lbl_1 _text--m_f6lbl_23').text
  potato_maxi_price = soup_maxi_potato.find('span', class_ = '_text_f6lbl_1 _text--m_f6lbl_23 utils__PriceText-sc-1fkdssq-0 ifeOmJ').text

  ica_maxi_chicken = requests.get('https://handlaprivatkund.ica.se/stores/1004219/categories/k%C3%B6tt-f%C3%A5gel-fisk/kyckling-f%C3%A5gel/kycklingfil%C3%A9/kycklingfil%C3%A9-fryst/5467bd65-83ff-46f1-89e0-9ced80fbd757?sortBy=favorite')
  soup_maxi_chicken = BeautifulSoup(ica_maxi_chicken.text, 'lxml')
  chicken_maxi_name = soup_maxi_chicken.find('h3', class_ = '_text_f6lbl_1 _text--m_f6lbl_23').text
  chicken_maxi_price = soup_maxi_chicken.find('span', class_ = '_text_f6lbl_1 _text--m_f6lbl_23 utils__PriceText-sc-1fkdssq-0 ifeOmJ').text

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
   maxi_cell7_id = 'maxi_potato_name'
   maxi_cell8_id = 'maxi_potato_price'
   maxi_cell9_id = 'maxi_chicken_name'
   maxi_cell10_id = 'maxi_chicken_price'

   maxi_cell1= soup.find('td', id=maxi_cell1_id)
   maxi_cell2= soup.find('td', id=maxi_cell2_id)
   maxi_cell3= soup.find('td', id=maxi_cell3_id)
   maxi_cell4= soup.find('td', id=maxi_cell4_id)
   maxi_cell5= soup.find('td', id=maxi_cell5_id)
   maxi_cell6= soup.find('td', id=maxi_cell6_id)
   maxi_cell7= soup.find('td', id=maxi_cell7_id)
   maxi_cell8= soup.find('td', id=maxi_cell8_id)
   maxi_cell9= soup.find('td', id=maxi_cell9_id)
   maxi_cell10= soup.find('td', id=maxi_cell10_id)
  
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

     #Update the content of the cheese name cell

  if maxi_cell3:
     maxi_cell3.string = cheese_maxi_name
  else:
     print(f"No cell found")

     #Update the content of the cheese price cell

  if maxi_cell4:
     maxi_cell4.string = cheese_maxi_price
  else:
     print(f"No cell found")

  if maxi_cell5:
     maxi_cell5.string = fish_maxi_name
  else:
     print(f"No cell found")

  if maxi_cell6:
     maxi_cell6.string = fish_maxi_price
  else:
     print(f"No cell found")

  if maxi_cell7:
     maxi_cell7.string = potato_maxi_name
  else:
     print(f"No cell found")

  if maxi_cell8:
     maxi_cell8.string = potato_maxi_price
  else:
     print(f"No cell found")

  if maxi_cell9:
     maxi_cell9.string = chicken_maxi_name
  else:
    print(f"No cell found")

  if maxi_cell10:
     maxi_cell10.string = chicken_maxi_price
  else:
     print(f"No cell found")

  with open(file_path, 'w') as file:
     file.write(str(soup))

  