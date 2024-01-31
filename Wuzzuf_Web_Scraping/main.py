import requests
from bs4 import BeautifulSoup
import pandas as pd

# Getting response from website
response = requests.get("https://wuzzuf.net/search/jobs/?q=machine+learning&a=hpb")
soup = BeautifulSoup(response.content,"lxml")

# Getting job titles
titles = soup.findAll("h2",{"class":"css-m604qf"})
titles_lst = [ i.text for i in titles]

# Getting job link 
links = soup.findAll("h2",{"class":"css-m604qf"})
links_lst = [i.a['href'] for i in links]

# Getting companies names
compaines = soup.findAll("div",{"class":"css-d7j1kk"})
compaines_lst = [ i.a.text.replace('-',' ').strip() for i in compaines]

# Getting companies locations
location = soup.find_all("span",{"class","css-5wys0k"})
location_lst = [i.text for i in location]

# Getting job specs
specs = soup.find_all("div",{"class","css-y4udm8"})
specs_lst = [i.text for i in specs]

# Scraped Data 
scraped = {}
scraped['Title'] = titles_lst
scraped['Link'] = links_lst
scraped['Company'] = compaines_lst
scraped['Location'] = location_lst
scraped['Specs'] = specs_lst

# To Data Frame
df = pd.DataFrame(scraped)

# To CSV file
df.to_csv('mljobs.csv',index=False)