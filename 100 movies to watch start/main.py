import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

def get_movies():
    movies_data = soup.find_all(name="h3", class_="title")

    titles = [movie.getText() for movie in movies_data]
    movies = titles[::-1]
    return movies

def save_movies(movies):
    with open("movies.txt", mode="w") as file:
        for movie in movies:
            file.write(f"{movie}\n")


movie_names = get_movies()
# print(movie_names)
save_movies(movie_names)
