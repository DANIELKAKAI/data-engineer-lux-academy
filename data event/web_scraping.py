import requests

from bs4 import BeautifulSoup

# <h2>
# <a href="/job/python-nlp-intern-elloe">Python/NLP Intern at Elloe n</a>
# </h2>

response = requests.get("https://www.myjobmag.co.ke/search/jobs?q=python--data+science")

html_doc = response.content

# print(html_doc)

soup = BeautifulSoup(html_doc, 'html.parser')

h2_tags = soup.find_all("h2")

#print(h2_tags)

for h2_tag in h2_tags:
    a_tag = h2_tag.a
    if a_tag is not None:
        title = a_tag.text
        url = a_tag["href"]
        full_url = "https://www.myjobmag.co.ke" + url
        print(title, full_url)

