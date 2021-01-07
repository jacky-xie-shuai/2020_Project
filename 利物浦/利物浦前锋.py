from bs4 import BeautifulSoup
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

import re

path = 'D:/1/利物浦/Liverpool.html'
htmlfile = open(path, 'r', encoding='gbk')
htmlhandle = htmlfile.read()

soup = BeautifulSoup(htmlhandle, 'html.parser')
qf_table = soup.find('table', class_='lqiuy_list lqiuy_list_qf ltable ltable_auto lmb jTrHover')
all_qf_players = qf_table.find('tbody')

qf_name = []
qf_age = []
qf_appearence = []
qf_minutes = []
qf_goal = []
qf_assist = []
qf_marketvalue = []

each_qf_player = all_qf_players.find_all('tr')[0]
all_td_tag = each_qf_player.find_all('td')

Name_txt = all_td_tag[3].text
searchObj = re.search(r'[\u2E80-\u9FFF]+', Name_txt, re.M | re.I)
if searchObj:
    Name = searchObj.group(0)
Age = all_td_tag[5].text
Appearence = all_td_tag[8].text
Goal = all_td_tag[10].text
Assist = all_td_tag[11].text
MarketValue_txt = all_td_tag[14].text
searchObj = re.search(r'\d{2}?', MarketValue_txt, re.M | re.I)
if searchObj:
    MarketValue = searchObj.group(0)

qf_name.append(Name)
qf_age.append(Age)
qf_appearence.append(Appearence)
qf_goal.append(Goal)
qf_assist.append(Assist)
qf_marketvalue.append(MarketValue)

for i in range(1, len(all_qf_players.find_all('tr'))):
    each_qf_player = all_qf_players.find_all('tr')[i]
    all_td_tag = each_qf_player.find_all('td')

    Name_txt = all_td_tag[2].text
    searchObj = re.search(r'[\u2E80-\u9FFF]+', Name_txt, re.M | re.I)
    if searchObj:
        Name = searchObj.group(0)
    Age = all_td_tag[4].text
    Appearence = all_td_tag[7].text
    Goal = all_td_tag[9].text
    Assist = all_td_tag[10].text
    MarketValue_txt = all_td_tag[13].text
    searchObj = re.search(r'\d{2}?', MarketValue_txt, re.M | re.I)
    if searchObj:
        MarketValue = searchObj.group(0)
    print(MarketValue)
    qf_name.append(Name)
    qf_age.append(Age)
    qf_appearence.append(Appearence)
    qf_goal.append(Goal)
    qf_assist.append(Assist)
    qf_marketvalue.append(MarketValue)


def bar_base() -> Bar:
    print(qf_name)
    c = (
        Bar({"theme": ThemeType.MACARONS})

            .add_xaxis(qf_name)
            .add_yaxis('身价/百万欧元', qf_marketvalue, category_gap="80%")
            .add_yaxis('年龄/岁', qf_age)
            .add_yaxis('出场/次', qf_appearence)
            .add_yaxis('进球', qf_goal)
            .add_yaxis('助攻', qf_assist)
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(name="球员姓名", axislabel_opts=opts.LabelOpts(rotate=-12)),
            title_opts=opts.TitleOpts(title="利物浦", subtitle="前锋一览"),
        )

    )
    c.render('Liverpool_qf.html')


bar_base()