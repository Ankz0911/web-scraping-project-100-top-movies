from bs4 import BeautifulSoup
import requests

yc_page = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(yc_page.text, "html.parser")
articles_list_unsorted = []
for article in soup.find_all('h3', class_="title"):
    articles_list_unsorted.append(article.getText())
final_list = [ele for ele in reversed(articles_list_unsorted)]

with open('movies.txt', mode="w") as file:
    for movie in final_list:
        file.write(f"{movie}\n")
