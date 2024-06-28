from bs4 import BeautifulSoup
import requests

def update_coop_data():

  coop_mince = requests.get('https://www.coop.se/handla/sok/?q=blandf%C3%A4rs')
  soup_coop_mince = BeautifulSoup(coop_mince.text, 'lxml')
  mince_coop_name = soup_coop_mince.find('p', class_ = 'ProductTeaser-heading').text
  mince_coop_price = soup_coop_mince.find('span', class_ = 'wqjVwCAg X7I7xYL7').text

  coop_cheese = requests.get('https://www.coop.se/handla/sok/?q=ost')
  soup_coop_cheese = BeautifulSoup(coop_cheese.text, 'lxml')
  cheese_coop_name = soup_coop_cheese.find('p', class_ = 'ProductTeaser-heading').text
  cheese_coop_price = soup_coop_cheese.find('span', class_ = 'wqjVwCAg X7I7xYL7').text

  coop_fish = requests.get('https://www.coop.se/handla/sok/?q=fisk')
  soup_coop_fish = BeautifulSoup(coop_fish.text, 'lxml')
  fish_coop_name = soup_coop_fish.find('p', class_ = 'ProductTeaser-heading').text
  fish_coop_price = soup_coop_fish.find('span', class_ = 'wqjVwCAg X7I7xYL7').text

  coop_potato = requests.get('https://www.coop.se/handla/sok/?q=potatis')
  soup_coop_potato = BeautifulSoup(coop_potato.text, 'lxml')
  potato_coop_name = soup_coop_potato.find('p', class_ = 'ProductTeaser-heading').text
  potato_coop_price = soup_coop_potato.find('span', class_ = 'wqjVwCAg X7I7xYL7').text

  coop_chicken = requests.get('https://www.coop.se/handla/sok/?q=kyckling')
  soup_coop_chicken = BeautifulSoup(coop_chicken.text, 'lxml')
  chicken_coop_name = soup_coop_chicken.find('p', class_ = 'ProductTeaser-heading').text
  chicken_coop_price = soup_coop_chicken.find('span', class_ = 'wqjVwCAg X7I7xYL7').text

# Reading existing HTML file
  file_path = 'templates/index.html'
  with open(file_path, 'r') as file:
   html_content = file.read()

  #Parseing the HTML content
   soup = BeautifulSoup(html_content,'lxml')

   #Locates the specific cell by id
   coop_cell1_id = 'coop_mince_name'
   coop_cell2_id = 'coop_mince_price'
   coop_cell3_id = 'coop_cheese_name'
   coop_cell4_id = 'coop_cheese_price'
   coop_cell5_id = 'coop_fish_name'
   coop_cell6_id = 'coop_fish_price'
   coop_cell7_id = 'coop_potato_name'
   coop_cell8_id = 'coop_potato_price'
   coop_cell9_id = 'coop_chicken_name'
   coop_cell10_id = 'coop_chicken_price'

   coop_cell1= soup.find('td', id=coop_cell1_id)
   coop_cell2= soup.find('td', id=coop_cell2_id)
   coop_cell3= soup.find('td', id=coop_cell3_id)
   coop_cell4= soup.find('td', id=coop_cell4_id)
   coop_cell5= soup.find('td', id=coop_cell5_id)
   coop_cell6= soup.find('td', id=coop_cell6_id)
   coop_cell7= soup.find('td', id=coop_cell7_id)
   coop_cell8= soup.find('td', id=coop_cell8_id)
   coop_cell9= soup.find('td', id=coop_cell9_id)
   coop_cell10= soup.find('td', id=coop_cell10_id)
  
   #Update the content of the mince name cell 
   if coop_cell1:
    coop_cell1.string = mince_coop_name
   else:
     print(f"No cell found")

   #Update the content of the mince price cell

  if coop_cell2:
     coop_cell2.string = mince_coop_price
  else:
     print(f"No cell found")

     #Update the content of the cheese name cell

  if coop_cell3:
     coop_cell3.string = cheese_coop_name
  else:
     print(f"No cell found")

     #Update the content of the cheese price cell

  if coop_cell4:
     coop_cell4.string = cheese_coop_price
  else:
     print(f"No cell found")

  if coop_cell5:
     coop_cell5.string = fish_coop_name
  else:
     print(f"No cell found")

  if coop_cell6:
     coop_cell6.string = fish_coop_price
  else:
     print(f"No cell found")

  if coop_cell7:
     coop_cell7.string = potato_coop_name
  else:
     print(f"No cell found")

  if coop_cell8:
     coop_cell8.string = potato_coop_price
  else:
     print(f"No cell found")

  if coop_cell9:
     coop_cell9.string = chicken_coop_name
  else:
    print(f"No cell found")

  if coop_cell10:
     coop_cell10.string = chicken_coop_price
  else:
     print(f"No cell found")

  with open(file_path, 'w') as file:
     file.write(str(soup))

  