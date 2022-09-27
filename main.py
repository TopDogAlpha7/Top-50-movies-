from urllib import request


import requests
import lxml
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

txt = response.text
soup = BeautifulSoup(txt, "lxml")
movies = soup.find_all(name="h3", class_="title")
all_movies = [movie.getText() for movie in movies]
order_movies = all_movies[::-1]


with open("list.txt", mode="w") as file:
    for movie in order_movies:
        file.write(f"{movie}\n")

