from bs4 import BeautifulSoup
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

import re

path = 'D:/1/巴黎/Paris.html'
htmlfile = open(path,'r',encoding = 'gbk')
htmlhandle = htmlfile.read()

soup = BeautifulSoup(htmlhandle, 'html.parser')
zc_table = soup.find('table',class_='lqiuy_list lqiuy_list_zc ltable ltable_auto lmb jTrHover' )

all_zc_players = zc_table.find('tbody')


zc_name = []
zc_age = []
zc_appearence = []
zc_minutes = []
zc_goal = []
zc_assist = []
zc_marketvalue = []


each_zc_player = all_zc_players.find_all('tr')[0]
all_td_tag = each_zc_player.find_all('td')

Name_txt = all_td_tag[3].text
searchObj = re.search(r'[\u2E80-\u9FFF]+', Name_txt, re.M | re.I)
if searchObj:
    Name = searchObj.group(0)
Age =  all_td_tag[5].text
Appearence = all_td_tag[8].text
Goal = all_td_tag[10].text
Assist = all_td_tag[11].text
MarketValue_txt = all_td_tag[14].text
searchObj = re.search(r'\d{2}?', MarketValue_txt, re.M | re.I)
if searchObj:
    MarketValue = searchObj.group(0)

zc_name.append(Name)
zc_age.append(Age)
zc_appearence.append(Appearence)
zc_goal.append(Goal)
zc_assist.append(Assist)
zc_marketvalue.append(MarketValue)

for i in range(1,len(all_zc_players.find_all('tr'))):
    each_zc_player = all_zc_players.find_all('tr')[i]
    all_td_tag = each_zc_player.find_all('td')

    Name_txt = all_td_tag[2].text
    searchObj = re.search(r'[\u2E80-\u9FFF]+', Name_txt, re.M | re.I)
    if searchObj:
        Name = searchObj.group(0)
    Age =  all_td_tag[4].text
    Appearence = all_td_tag[7].text
    Goal = all_td_tag[9].text
    Assist = all_td_tag[10].text
    MarketValue_txt = all_td_tag[13].text
    searchObj = re.search(r'\d{2}?', MarketValue_txt, re.M | re.I)
    if searchObj:
        MarketValue = searchObj.group(0)
    print(MarketValue)
    zc_name.append(Name)
    zc_age.append(Age)
    zc_appearence.append(Appearence)
    zc_goal.append(Goal)
    zc_assist.append(Assist)
    zc_marketvalue.append(MarketValue)

def bar_base() -> Bar:
    print(zc_name)
    c = (
        Bar({"theme": ThemeType.MACARONS})

        .add_xaxis(zc_name)
        .add_yaxis('身价/百万欧元',zc_marketvalue,category_gap="80%")
        .add_yaxis('年龄/岁',zc_age)
        .add_yaxis('出场/次',zc_appearence)
        .add_yaxis('进球',zc_goal)
        .add_yaxis('助攻',zc_assist)
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(name="球员姓名",axislabel_opts=opts.LabelOpts(rotate=-12)),
            title_opts=opts.TitleOpts(title="巴黎",subtitle="中场一览"),
        )


    )
    c.render('Paris_zc.html')
bar_base()





