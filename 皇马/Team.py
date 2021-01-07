import requests
from pyecharts.globals import SymbolType
from bs4 import BeautifulSoup
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Page, Pie
from pyecharts import options as opts
import csv
from pyecharts.charts import Page, Pie, Bar

#1-2.直接抓取、解析
url = "https://liansai.500.com/team/883/"
response = requests.get(url)
soup = BeautifulSoup(response.content.decode('gbk'), 'html.parser')

#2.获取并分析元素
all_data = soup.find('tbody', class_ = "jTrInterval")
teamName=soup.find('h2', class_ = "lsnav_qdnav_name")
print(teamName.text)

#写模式打开csv文件
csv_obj = open('data.csv', 'w')

#写入一行标题
csv.writer(csv_obj).writerow(["League", "Date", "HomeTeam", "Score", "Vistor", "Result"])
#print(all_movies)
#3.展示有用信息
all_player = []
for each_player in all_data.find_all('tr'):
    #print(each_movie)
    all_td_tag = each_player.find_all('td')
    League =  all_td_tag[0].text
    Date =  all_td_tag[1].text
    HomeTeam =  all_td_tag[2].text
    Score =  all_td_tag[3].text
    Vistor = all_td_tag[4].text
    Result = all_td_tag[5].text
    #获取 球队信息：俱乐部 日期 主场 比分 客场 结果
    all_player.append({'League': League,
                       'Date': Date,
                       'HomeTeam': HomeTeam,
                       'Score': Score,
                       'Vistor': Vistor,
                       'Result': Result})
    League = League.strip()
    Date = Date.strip()
    HomeTeam = HomeTeam.strip()
    Score = Score.strip()
    Vistor = Vistor.strip()
    Result = Result.strip()
    print(League)
    print(Date)
    print(HomeTeam)
    print(Score)
    print(Vistor)
    print(Result)
    # csv.writer(csv_obj).writerow([League, Date, HomeTeam, Score, Vistor, Result])
csv_obj.close()
print(all_player)
League = [l['League'] for l in all_player]
Date = [l['Date'] for l in all_player]
HomeTeam = [l['HomeTeam'] for l in all_player]
Score = [l['Score'] for l in all_player]
Vistor = [l['Vistor'] for l in all_player]
Result = [l['Result'] for l in all_player]

def winRate():
    print(Result)
    CountWin=Result.count('胜')
    CountLose = Result.count('负')
    CountTie = Result.count('平')
    attr = ["胜", "平", "负"]
    v1=[CountWin,CountTie,CountLose]
    c = (
        Pie()
            .add("", [list(z) for z in zip(attr, v1)])
            .set_global_opts(title_opts=opts.TitleOpts(title=teamName.text+"近期胜率"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    c.render('pie.html')
winRate()
