from bs4 import BeautifulSoup
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

import re

path = 'D:/1/巴萨/Barca.html'
htmlfile = open(path,'r',encoding = 'gbk')
htmlhandle = htmlfile.read()

soup = BeautifulSoup(htmlhandle, 'html.parser')
hw_table = soup.find('table',class_='lqiuy_list lqiuy_list_hw ltable ltable_auto lmb jTrHover' )

all_hw_players = hw_table.find('tbody')


hw_name = []
hw_age = []
hw_appearence = []
hw_minutes = []
hw_goal = []
hw_assist = []
hw_marketvalue = []


each_hw_player = all_hw_players.find_all('tr')[0]
all_td_tag = each_hw_player.find_all('td')

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

hw_name.append(Name)
hw_age.append(Age)
hw_appearence.append(Appearence)
hw_goal.append(Goal)
hw_assist.append(Assist)
hw_marketvalue.append(MarketValue)

for i in range(1,len(all_hw_players.find_all('tr'))):
    each_hw_player = all_hw_players.find_all('tr')[i]
    all_td_tag = each_hw_player.find_all('td')

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
    hw_name.append(Name)
    hw_age.append(Age)
    hw_appearence.append(Appearence)
    hw_goal.append(Goal)
    hw_assist.append(Assist)
    hw_marketvalue.append(MarketValue)

def bar_base() -> Bar:
    print(hw_name)
    c = (
        Bar({"theme": ThemeType.MACARONS})

        .add_xaxis(hw_name)
        .add_yaxis('身价/百万欧元',hw_marketvalue,category_gap="80%")
        .add_yaxis('年龄/岁',hw_age)
        .add_yaxis('出场/次',hw_appearence)
        .add_yaxis('进球',hw_goal)
        .add_yaxis('助攻',hw_assist)
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(name="球员姓名",axislabel_opts=opts.LabelOpts(rotate=-12)),
            title_opts=opts.TitleOpts(title="巴萨",subtitle="后卫一览"),
        )


    )
    c.render('Barca_hw.html')
bar_base()





