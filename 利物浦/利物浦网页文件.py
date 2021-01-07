import requests

url = "http://liansai.500.com/team/1011/teamlineup/"
response = requests.get(url)

file_obj = open('Liverpool.html', 'w')
file_obj.write(response.content.decode('gbk'))
file_obj.close()

