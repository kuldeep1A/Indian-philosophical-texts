import bs4
import urllib.request
import os
import dotenv
dotenv.load_dotenv()
URL = os.getenv("URL")
while True:
    try:
        html_content = urllib.request.urlopen(URL).read()
        break
    except ExceptionGroup:
        pass

html_string = html_content.decode(errors="ignore")
html_content = html_string.replace('\r', '')
soup = bs4.BeautifulSoup(html_content, 'html.parser')
filed = soup.findAll('div', {'class': 'field-content'})
print(filed)