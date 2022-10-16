import requests
from bs4 import BeautifulSoup
#import CSV

page = requests.get("https://raw.githack.com/paskorn/DS270-Git2022/master/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify()) #display html source code
#print( list(soup.children))
#print([type(item) for item in list(soup.children)])

#We can now select the html tag and its children by taking the third item in the list:
html = list(soup.children)[2]
#print(list(html))
#print("---------------------------------")
#print(list(html.children))

#As we can see above, there are two tags here, head, and body. 
#We want to extract the text inside the p tag, 
#so we’ll dive into the body:
body = list(html.children)[3]
#print(list(body.children))


p = list(body.children)[1]
#print(p.get_text())

print(soup.find_all('p'))
print(soup.find_all('p')[0])
print(soup.find_all('p')[0].get_text())
print(soup.find_all('p')[1])
print(soup.find_all('p')[1].get_text())
 


