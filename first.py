import matplotlib.pyplot as plt
import matplotlib
from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%97%AD%EB%8C%80%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84') as response:
    soup = BeautifulSoup(response,'html.parser')
    #print(soup)

    movie = soup.find('div',{'class':'_content'})

    movie_name = movie.select('strong')
    movie_name1 = []
    for i in movie_name:
        movie_name1.append(i.text)
    # print(movie_name1)
#여기까지 '추정훈'의 크롤러 코딩

    rank = 1
    for name in movie_name1:
        print(str(rank) + " 위 : " + name)
        rank += 1
#여기까지 '추정훈'의 그래프 코딩