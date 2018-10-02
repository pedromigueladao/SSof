### Pedro Adao, 2017
# This file has most of the examples one needs to use requests.

import requests

SERVER=''


#### GET REQUESTS
params = {'field1' : 'value1', 'field2' : 'value2'}
headers = {'user-agent': 'my-app/0.0.1', 'Content-Type': 'application/json'}
r = requests.get(SERVER, params=params, headers=headers)

#### POST REQUESTS
data = {'field1' : 'value1', 'field2' : 'value2'}
headers = {'user-agent': 'my-app/0.0.1', 'Content-Type': 'application/json'}
r = requests.post(SERVER, data=data, headers=headers)

#### PUT REQUESTS
params = {'field1' : 'value1', 'field2' : 'value2'}
data = {'field1' : 'value1', 'field2' : 'value2'}
headers = {'user-agent': 'my-app/0.0.1', 'Content-Type': 'application/json'}
r = requests.put(SERVER, params=payload, data=data, headers=headers)



#### ANSWERS
print 'status     : ', r.status_code
print 'headers    : ', r.headers
print 'cookies    : ', r.cookies
print 'html       : ', r.text



##### AUTHENTICATION
params = {'field1' : 'value1', 'field2' : 'value2'}
headers = {'user-agent': 'my-app/0.0.1', 'Content-Type': 'application/json'}
user ='XXX'
passwd = 'YYY'
r = requests.get(SERVER, params=params, headers=headers, auth=(user, passwd)) ### Same for other methods



##### COOKIES

#### Extract Cookie values
cookie_value = r.cookies['field']

#### Update and send new cookie values
data = {'field1' : 'value1', 'field2' : 'value2'}
cookies = {'field1' : 'value1', 'field2' : 'value2'}
r = requests.get(SERVER, data=data, cookies=cookies) ### Same for other methods



##### WITH SESSIONS
# start session
session = requests.session()

params = {'field1' : 'value1', 'field2' : 'value2'}
r = session.get(SERVER, params=params) ### Same for other methods
all_cookies = requests.utils.dict_from_cookiejar(session.cookies)

# update and resend cookies
session.cookies.set('field', 'new_value', domain='domain_of_cookie', path='path_of_cookie')
r = session.get(SERVER, params=params) ### Same for other methods



##### WITH SOCKS PROXY WE SET UP VIA
# ssh -D 4444 -i <private key file path> -p <port> <user>@<ipaddress>
proxies = {'http': "socks5://localhost:4444"}

params = {'field1' : 'value1', 'field2' : 'value2'}
headers = {'user-agent': 'my-app/0.0.1', 'Content-Type': 'application/json'}
r = requests.get(SERVER, params=params, headers=headers, proxies=proxies)