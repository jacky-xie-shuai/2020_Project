import requests

url = "http://liansai.500.com/team/653/teamlineup/"
response = requests.get(url)

file_obj = open('Barca.html', 'w')
file_obj.write(response.content.decode('gbk'))
file_obj.close()

