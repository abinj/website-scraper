from urllib2 import urlopen
from bs4 import BeautifulSoup



url = "https://www.mathematicalmichael.com/"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
text = soup.find_all('body')
print(text)
