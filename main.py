import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL).text

soup = BeautifulSoup(response, 'html.parser')
top_films = []
content = soup.find_all(name='h3', class_='title')
for film in content:
    top_film = film.getText()
    top_films.append(top_film)

top_films.reverse()

with open('films_to_watch.txt', 'w') as f:
    for film in top_films:
        f.write(film + '\n')




