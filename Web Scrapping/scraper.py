# importing the libraries
from bs4 import BeautifulSoup
import requests

# let's parse out the article headline and summaries from the simple.html file
# Creating BeautifulSoup object passing the html file
with open('simple.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# let's print the object
# print(soup)                 # This will print the entire html
# print(soup.prettify())      # This will print the entire html in indented manner


# accessing information from a tag
# getting the title of the html page
# if we only want the text of the tag then use the 'text' attribute

# match = soup.title
# match = soup.title.text
# print(match)

# Now if there are multiple same tag names like 'div' then previous way only return the first match
# But if we want the div tag that has the class 'footer' then we need to use the find()
# Here we use 'class_' as a parameter to find the class because 'class' is a keyword in python

# match = soup.div
# match = soup.find('div', class_='footer')
# print(match)


# Now fetching all the headlines and summaries of the page
# This is to get information just for the 1st article class

# article = soup.find('div', class_='article')
# print(article)

# headline = article.h2.a.text
# print(headline)

# summary = article.p.text
# print(summary)


# Now to get information from all the articles
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()