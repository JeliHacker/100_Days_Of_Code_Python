from bs4 import BeautifulSoup


with open("website.html") as html_file:
    contents = html_file.read()

soup = BeautifulSoup(contents, "html.parser")

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))

heading = soup.find_all(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
#print(section_heading.get("class"))

company_url = soup.select_one(selector="#name")
print(company_url)

headings = soup.select(".heading")
print(headings)