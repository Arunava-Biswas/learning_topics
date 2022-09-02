# importing libraries
from bs4 import BeautifulSoup
import requests
import csv

# getting the source code from the website
# this requests.get() will return a response object
# to get the code we need to add the '.text' at the end
# now the source variable will be equal to the html of that website
source = requests.get('http://coreyms.com').text

# creating object of the html we get from source
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

# creating the csv file to store the fetched data
csv_file = open('csv_file//cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
# creating the headers
csv_writer.writerow(['Headline', 'Summary', 'Video_link'])

# creating a loop to fetch the data
for article in soup.find_all('article'):
    # title part
    headline = article.h2.a.text
    print(headline)

    # summary part
    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    # video link part
    # here the videos are embedded to the 'iframe' tag i.e. it is not a direct link to the video itself
    # so here we need to grab the value from the source attribute from the iframe tag by using the ['src']
    # if we want to get the attribute of a tag then we can access it like a dictionary
    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        # so here we need to get the video id separated from the query which started after the '?' in the url
        # we needed the 4th index of the returned list in vid_id
        vid_id = vid_src.split('/')[4]
        # now we need to split the vid_id on the basis of '?' so we can separate the id from the rest of the query
        # the vid_id is the 0th index of the list returned in vid_id
        vid_id = vid_id.split('?')[0]

        # here we are creating the youtube link using the vid_id we parsed
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        # if no youtube link can be found
        yt_link = None
        print(e)

    print(yt_link)

    print()
    # write the information to the csv file after each iteration
    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
