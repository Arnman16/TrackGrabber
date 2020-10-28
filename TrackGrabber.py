import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://open.spotify.com/playlist/3XflgZfMSSn7M2mK9BLZmM"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

title = soup.select('title')[0]
spans = soup.select('span')

playlist = {
    'Artist': [],
    'Track': [],
    'Album': [],
}

for span in spans:
    span_class = span.get('class')
    if span_class:
        if span_class[0] == 'track-name':
            playlist['Track'].append(span.text)
        if span_class[0] == 'artists-albums':
            artist_albums = span.text.replace(' ', '').split('•')
            playlist['Artist'].append(artist_albums[0])
            playlist['Album'].append(artist_albums[1])

playlist_df = pd.DataFrame(playlist)

print(title.text)
print(playlist_df)

