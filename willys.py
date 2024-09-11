from bs4 import BeautifulSoup


def update_willys_data():

  mince_willys_name = 'Blandfärs 20% Sverige 1kg'
  mince_willys_price = '92,90 kr/st'

  cheese_willys_name = 'Präst Mellanlagrad 31%'
  cheese_willys_price = '121,00 kr/st'

  fish_willys_name = 'Laxbitar Fryst 300g'
  fish_willys_price = '51,90 kr/st'

  potato_willys_name = 'Potatis Fast Klass 1'
  potato_willys_price = '19,90 kr/st'

  chicken_willys_name = 'Kycklingfilé Bröstfilé Sverige 850g'
  chicken_willys_price = '129 kr/kg'

# Reading existing HTML file
  file_path = 'templates/index.html'
  with open(file_path, 'r') as file:
   html_content = file.read()

  #Parseing the HTML content
   soup = BeautifulSoup(html_content,'lxml')

   #Locates the specific cell by id
   willys_cell1_id = 'willys_mince_name'
   willys_cell2_id = 'willys_mince_price'
   willys_cell3_id = 'willys_cheese_name'
   willys_cell4_id = 'willys_cheese_price'
   willys_cell5_id = 'willys_fish_name'
   willys_cell6_id = 'willys_fish_price'
   willys_cell7_id = 'willys_potato_name'
   willys_cell8_id = 'willys_potato_price'
   willys_cell9_id = 'willys_chicken_name'
   willys_cell10_id = 'willys_chicken_price'

   willys_cell1= soup.find('td', id=willys_cell1_id)
   willys_cell2= soup.find('td', id=willys_cell2_id)
   willys_cell3= soup.find('td', id=willys_cell3_id)
   willys_cell4= soup.find('td', id=willys_cell4_id)
   willys_cell5= soup.find('td', id=willys_cell5_id)
   willys_cell6= soup.find('td', id=willys_cell6_id)
   willys_cell7= soup.find('td', id=willys_cell7_id)
   willys_cell8= soup.find('td', id=willys_cell8_id)
   willys_cell9= soup.find('td', id=willys_cell9_id)
   willys_cell10= soup.find('td', id=willys_cell10_id)
  
   #Update the content of the mince name cell 
   if willys_cell1:
    willys_cell1.string = mince_willys_name
   else:
     print(f"No cell found")

   #Update the content of the mince price cell

  if willys_cell2:
     willys_cell2.string = mince_willys_price
  else:
     print(f"No cell found")

     #Update the content of the cheese name cell

  if willys_cell3:
      willys_cell3.string = cheese_willys_name
  else:
     print(f"No cell found")

     #Update the content of the cheese price cell

  if willys_cell4:
     willys_cell4.string = cheese_willys_price
  else:
     print(f"No cell found")

  if willys_cell5:
     willys_cell5.string = fish_willys_name
  else:
     print(f"No cell found")

  if willys_cell6:
     willys_cell6.string = fish_willys_price
  else:
     print(f"No cell found")

  if willys_cell7:
     willys_cell7.string = potato_willys_name
  else:
     print(f"No cell found")

  if willys_cell8:
     willys_cell8.string = potato_willys_price
  else:
     print(f"No cell found")

  if willys_cell9:
     willys_cell9.string = chicken_willys_name
  else:
    print(f"No cell found")

  if willys_cell10:
     willys_cell10.string = chicken_willys_price
  else:
     print(f"No cell found")

  with open(file_path, 'w') as file:
     file.write(str(soup))