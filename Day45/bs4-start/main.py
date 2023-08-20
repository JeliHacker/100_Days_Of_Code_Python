from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
article_texts = []
article_links = []
for title in soup.find_all(name="span", class_="titleline"):
    text = title.text
    link = title.get('href')
    article_texts.append(text)
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts, len(article_texts))
print(article_links, len(article_links))
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(largest_index, largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])