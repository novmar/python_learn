import  requests
import bs4
headers = {
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
}

login_data = {
    'username': 'ubnt',
    'password': 'bot6pu5l',
    'form_id': 'loginform',
    'op': 'Login',
    'uri': '/index.cgi',
}
enable_https_data = {
    'httpds_status' : "enabed",
    'form_id':'svc_form',
}
proto="http://"
ip="10.32.166.26"
login_url = "/login.cgi"
services_url = "/services.cgi"
apply_url = "/apply.cgi"

with requests.Session() as s:
    r = s.get(proto+ip+login_url,headers=headers,verify=False)
    # soup= bs4.BeautifulSoup(r.content,'html.parser')
    # print (soup.prettify())
    r = s.post(proto+ip+login_url,data=login_data,verify=False)
    r = s.post(proto+ip+services_url,data=enable_https_data,verify=False)
    r = s.get(proto+ip+apply_url,headers=headers,verify=False)
