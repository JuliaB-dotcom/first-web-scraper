from bs4 import BeautifulSoup

def update_super_data():


  mince_super_name = 'Hushållsfärs Färsk 500g ICA'
  mince_super_price = '53,95 kr'
  
  cheese_super_name = 'Mild & Syrlig ost ca 500g Arla'
  cheese_super_price = '76,548 kr'

  fish_super_name = 'Alaska pollock Fryst 400g ICA Basic'
  fish_super_price = '35,95 kr'

  potato_super_name = 'Fast potatis 2kg Klass 1 ICA'
  potato_super_price = '39,95 kr'

  chicken_super_name = 'Kycklingfilé Fryst 1kg Kronfågel'
  chicken_super_price = '97,95 kr'

# Reading existing HTML file
  file_path = 'templates/index.html'
  with open(file_path, 'r') as file:
   html_content = file.read()

  #Parseing the HTML content
   soup = BeautifulSoup(html_content,'lxml')

   #Locates the specific cell by id
   super_cell1_id = 'super_mince_name'
   super_cell2_id = 'super_mince_price'
   super_cell3_id = 'super_cheese_name'
   super_cell4_id = 'super_cheese_price'
   super_cell5_id = 'super_fish_name'
   super_cell6_id = 'super_fish_price'
   super_cell7_id = 'super_potato_name'
   super_cell8_id = 'super_potato_price'
   super_cell9_id = 'super_chicken_name'
   super_cell10_id = 'super_chicken_price'
   super_cell1= soup.find('td', id=super_cell1_id)
   super_cell2= soup.find('td', id=super_cell2_id)
   super_cell3= soup.find('td', id=super_cell3_id)
   super_cell4= soup.find('td', id=super_cell4_id)
   super_cell5= soup.find('td', id=super_cell5_id)
   super_cell6= soup.find('td', id=super_cell6_id)
   super_cell7= soup.find('td', id=super_cell7_id)
   super_cell8= soup.find('td', id=super_cell8_id)
   super_cell9= soup.find('td', id=super_cell9_id)
   super_cell10= soup.find('td',id=super_cell10_id)
  
   #Update the content of the mince name cell 
   if super_cell1:
    super_cell1.string = mince_super_name
   else:
     print(f"No cell found")

   #Update the content of the mince price cell

  if super_cell2:
     super_cell2.string = mince_super_price
  else:
     print(f"No cell found")

     #Update the content of the cheese name cell

  if super_cell3:
     super_cell3.string = cheese_super_name
  else:
     print(f"No cell found")

     #Update the content of the cheese price cell

  if super_cell4:
     super_cell4.string = cheese_super_price
  else:
     print(f"No cell found")

  if super_cell5:
     super_cell5.string = fish_super_name
  else:
     print(f"No cell found")

  if super_cell6:
     super_cell6.string = fish_super_price
  else:
     print(f"No cell found")

  if super_cell7:
     super_cell7.string = potato_super_name
  else:
     print(f"No cell found")

  if super_cell8:
     super_cell8.string = potato_super_price
  else:
     print(f"No cell found")

  if super_cell9:
     super_cell9.string = chicken_super_name
  else:
    print(f"No cell found")

  if super_cell10:
     super_cell10.string = chicken_super_price
  else:
     print(f"No cell found")

  with open(file_path, 'w') as file:
     file.write(str(soup))

  