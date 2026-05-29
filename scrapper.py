import requests
from bs4 import BeautifulSoup
import datetime


url = "https://pixelford.com/blog"
response = requests.get(url, headers = {'user-agent': 'Hello'})
html = response.content

soup = BeautifulSoup(html, 'html.parser')
blogs = soup.find_all('article', class_="type-post")
for blog in blogs:
    title = blog.find('a', class_= "entry-title-link").get_text()
    date = blog.find('time', class_="entry-time").get('datetime')
    date_simplified = datetime.datetime.fromisoformat(date)
    pretty_date = date_simplified.strftime("%b %d %Y ")
    print(f"{pretty_date} -  {title}")




