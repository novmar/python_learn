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
function ubnt_login(ip,user,password,secure=False)

