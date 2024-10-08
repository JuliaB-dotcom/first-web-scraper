from bs4 import BeautifulSoup
import requests

def update_coop_data():

  mince_coop_name = 'Nötfärs 12% 1000g'
  mince_coop_price = '114,00 kr'

  cheese_coop_name = 'Präst ost 750g'
  cheese_coop_price = '90,00 kr'

  fish_coop_name = 'Alaska Pollock 4-pack 400g'
  fish_coop_price = '39,95 kr'

  potato_coop_name = 'Färskpotatis'
  potato_coop_price = '19,95 kr'

  chicken_coop_name = 'Kycklingfilé 100g'
  chicken_coop_price = '95 kr'

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

  