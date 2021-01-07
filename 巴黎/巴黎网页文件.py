import requests

url = "http://liansai.500.com/team/647/teamlineup/"
response = requests.get(url)

file_obj = open('Paris.html', 'w')
file_obj.write(response.content.decode('gbk'))
file_obj.close()

