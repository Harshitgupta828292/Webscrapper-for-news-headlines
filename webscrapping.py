import requests
from bs4 import BeautifulSoup
URL='https://www.bbc.com/news'
response=requests.get(URL)
print("the response code is :",response)
# parse the HTML Document
soup=BeautifulSoup(response.content,'html.parser')
# Extract the news Headline from HTML
headlines=soup.find_all('h2')
with open(".txt","w") as file:
    for headline in headlines:
        text=headline.get_text(strip=True)
        file.write(text+"\n")
        # print the news headline from html 
print(headline.text,"/n")
