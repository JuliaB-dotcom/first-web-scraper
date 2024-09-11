from bs4 import BeautifulSoup
import requests

def update_maxi_data():


  mince_maxi_name = 'Blandfärs 50/50 18% 500g KRAV ICA I love eco'
  mince_maxi_price = '55,95 kr'
  
  cheese_maxi_name = 'Mild & Syrlig ost ca 500g Arla'
  cheese_maxi_price = '72,50 kr'

  fish_maxi_name = 'Fiskköttbullar 400g Gårdsfisk'
  fish_maxi_price = '65,95 kr'

  potato_maxi_name = 'Potatis Fast 1,2kg Klass 1 ICA'
  potato_maxi_price = '33,95 kr'

  chicken_maxi_name = 'Kycklingfilé Fryst 1kg Kronfågel'
  chicken_maxi_price = '99,95 kr'

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

  