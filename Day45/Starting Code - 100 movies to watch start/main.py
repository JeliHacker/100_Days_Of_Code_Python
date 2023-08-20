import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)

webpage_html = response.text
soup = BeautifulSoup(webpage_html, "html.parser")

# print(soup.prettify())
titles = soup.find_all("h3", class_="title")
titles_text = [title.text for title in titles]
print(type(titles_text), titles_text)

with open("movies.txt", "w") as file:
    for title in titles_text[::-1]:
        file.write(title + "\n")


