from bs4 import BeautifulSoup
import requests

ica_maxi_mince = requests.get('https://handlaprivatkund.ica.se/stores/1004219/search?onOffer=onOffer&q=Blandf%C3%A4rs&sortBy=favorite')
soup_mince = BeautifulSoup(ica_maxi_mince.text, 'lxml')
mince_name = soup_mince.find('a', class_ = 'link__Link-sc-14ymsi2-0 cgxCVj link__Link-sc-14ymsi2-0 base__Title-sc-1mnb0pd-27 base__FixedHeightTitle-sc-1mnb0pd-43 cgxCVj ctGnCh cCRJZx').text

print(mince_name)