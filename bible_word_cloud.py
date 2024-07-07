import requests
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import sys, os
os.chdir(sys.path[0])

base_url = 'https://bible-api.com/'

print('Enter book of the Bible:')
bible_book = input()
print('Enter chapter number:')
bible_chapter = input()
print('Enter verse number(s):')
bible_verses = input()

full_url = f"{base_url}{bible_book}+{bible_chapter}:{bible_verses}"
response = requests.get(full_url)
text = response.json()['text']
stopwords = STOPWORDS

wc = WordCloud(
    background_color = 'white',
    stopwords = stopwords,
    height = 600,
    width = 400
    )

wc.generate(text)
wc.to_file('wordcloud_output.png')