import requests
from lxml import html

session_req = requests.session()

login_url = 'http://10.1.2.12/auth1.html'
result = session_req.get(login_url)

tree = html.fromstring(result.text)
token = list(set(tree.xpath("//input[@name='sessId']/@value")))[0]
param1 = list(set(tree.xpath("//input[@name='param1']/@value")))[0]
param2 = list(set(tree.xpath("//input[@name='param2']/@value")))[0]

user = 'john.cook'
password = 'Flutt3r$hy99!'

payload = {
	"param1": param1,
	"param2": param2,
        "id": user,
	"uName": user, 
        "userName": "",
	"pass": password,
	"pwd": password,
	"sessId": token,
}

login_url = 'http://10.1.2.12/auth.cgi'

result = session_req.post(
	login_url, 
	data = payload, 
	headers = dict(referer=login_url)
)

print result.content

print result.status_code

