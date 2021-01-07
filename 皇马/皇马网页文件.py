import requests

url = "http://liansai.500.com/team/883/teamlineup/"
response = requests.get(url)

file_obj = open('RealMadrid.html', 'w')
file_obj.write(response.content.decode('gbk'))
file_obj.close()




