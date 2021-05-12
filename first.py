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

    movie_content = movie.select('dd')
    x = []
    movie_poplaration=[]
    for i in movie_content:
        x.append(i.text)
    for j in range(len(movie_content)):
        if j % 2 == 1:
            movie_poplaration.append(x[j])
    # print(movie_poplaration)

    y=[]
    movie_update = []
    for i in movie_content:
        y.append(i.text)
    for j in range(len(movie_content)):
        if j % 2 == 0 :
            movie_update.append(y[j])
    # print(movie_update)

    name_date = []
    for i in range(len(movie_update)):
        name_date.append(movie_name1[i]+'\n'+movie_update[i])
    # print(name_date)
#여기까지 '이은희'의 크롤러 코딩

    figure = []
    for i in range(len(movie_poplaration)):
        k = movie_poplaration[i]
        p = k[0] + k[1] + k[3] + k[4] + k[5] + k[7] + k[8] + k[9]
        p = int(p)
        figure.append(p)
#    print(figure)
#여기까지 '추정훈'의 리스트 원소 변환 코딩