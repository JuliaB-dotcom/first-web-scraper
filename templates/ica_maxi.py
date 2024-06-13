from bs4 import BeautifulSoup
import requests

ica_maxi_mince = requests.get('https://handlaprivatkund.ica.se/stores/1004219/search?q=blandf%C3%A4rs&sortBy=pricePerDescending')
soup_mince = BeautifulSoup(ica_maxi_mince.text, 'lxml')
mince_name = soup_mince.find('a', class_ = 'link__Link-sc-14ymsi2-0 cgxCVj link__Link-sc-14ymsi2-0 base__Title-sc-1mnb0pd-27 base__FixedHeightTitle-sc-1mnb0pd-43 cgxCVj ctGnCh cCRJZx').text
mince_price = soup_mince.find(class_ = 'div', class_ = 'base__PriceWrapper-sc-1mnb0pd-28 dDLLyP').text
mince_info =  mince_name + '' + mince_price

# Reading existing HTML file
file_path = 'index.html'
with open(file_path, 'r')as file:
  html_content = file.read()

  #Parseing the HTML content
  soup = BeautifulSoup(html_content,'lxml')

  #Locates the table with HTML
  table = soup.find('table')

  #Creates a new row and adds the mince_name to it 

  new_row = soup.new_tag('tr')
  mince_cell = soup.new_tag('td')
  mince_cell.string = mince_info
  new_row.append(mince_cell)

  mince_cell2 = soup.new_tag('td')
  mince_cell2.string = mince_info
  new_row.append(mince_cell2)

  mince_cell3 = soup.new_tag('td')
  mince_cell3.string = mince_info
  new_row.append(mince_cell3)

  mince_cell4 = soup.new_tag('td')
  mince_cell4.string = mince_info
  new_row.append(mince_cell4)

  table.append(new_row)

  with open(file_path, 'w') as file:
    file.write(str(soup))

print(mince_name)