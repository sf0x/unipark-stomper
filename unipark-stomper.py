import requests
import re
from subprocess import check_output
from random import randint
import time

def timer(button):
  return randint(button*6,button*14)


r=requests.get('https://unipark.de/#placeholder#')
cookies=r.cookies
returl=str(r.url)
SES=re.search("[abcdef0-9]{32}", returl).group()
SYD=re.search("syid=[0-9]{6}", returl).group()
SID=re.search("sid=[0-9]{6}", returl).group()
print(SES)
print(SID)
print(SYD)
PG=re.search("pg_code\"\svalue=\"[abcdef0-9]{17}\"",r.text).group()
syd=SYD[5]+SYD[6]+SYD[7]+SYD[8]+SYD[9]+SYD[10]
sid=SID[4]+SID[5]+SID[6]+SID[7]+SID[8]+SID[9]
pg_code=re.search("[a-f0-9]{17}",PG).group()

button=1 # needed to calc the delay length

headers = {
    'DNT': '1',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'de-DE,de;q=0.8,en-US;q=0.6,en;q=0.4',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Connection': 'keep-alive',
}


params = (
    ('SES', SES),
    #('syid', syd),
    #('sid', sid),
    #('act', 'start'),
)


data = [
  ('act', 'send'),
  ('pg_code', pg_code),
  ('__backb', '0'),
  ('__no_pc', '0'),
  ('submit_button', 'Weiter'),
]



time.sleep(timer(button))
v=requests.post('https://unipark.de/#placeholder##placeholder#', headers=headers, params=params, cookies=cookies, data=data)

#print(v)
print("1")

cookies=v.cookies

choose1=randint(1,8)
ch_stand=randint(1,5)

data = [
  ('act', 'send'),
  ('pg_code', pg_code),
  ('v_25', choose1),
  ('__backb', '0'),
  ('__no_pc', '0'),
  ('submit_button', 'Weiter'),
]
button=1

time.sleep(timer(button))
v=requests.post('https://unipark.de/#placeholder##placeholder#', headers=headers, params=params, cookies=cookies, data=data)

#print(v)
print("2")

cookies=v.cookies

data = [
  ('act', 'send'),
  ('pg_code', pg_code),
  ('v_2', ch_stand),
  ('__backb', '0'),
  ('__no_pc', '0'),
  ('submit_button', 'Weiter'),
]
button=1

time.sleep(timer(button))
v=requests.post('https://unipark.de/#placeholder##placeholder#', headers=headers, params=params, cookies=cookies, data=data)

#print(v)
print("3")

cookies=v.cookies


data = [
  ('act', 'send'),
  ('pg_code', pg_code),
  ('v_4', ch_stand),
  ('__backb', '0'),
  ('__no_pc', '0'),
  ('submit_button', 'Weiter'),
]
button=1

time.sleep(timer(button))
v=requests.post('https://unipark.de/#placeholder##placeholder#', headers=headers, params=params, cookies=cookies, data=data)

#print(v)
print("4")

cookies=v.cookies

data = [
  ('act', 'send'),
  ('pg_code', pg_code),
  ('v_5', ch_stand),
  ('v_6', ch_stand),
  ('v_7', ch_stand),
  ('__backb', '0'),
  ('__no_pc', '0'),
  ('submit_button', 'Weiter'),
]
button=3

time.sleep(timer(button))
v=requests.post('https://unipark.de/#placeholder##placeholder#', headers=headers, params=params, cookies=cookies, data=data)

#print(v)
print("5")

cookies=v.cookies


data = [
  ('act', 'send'),
  ('pg_code', pg_code),
  ('v_10', ch_stand),
  ('__backb', '0'),
  ('__no_pc', '0'),
  ('submit_button', 'Weiter'),
]
button=1

time.sleep(timer(button))
v=requests.post('https://unipark.de/#placeholder##placeholder#', headers=headers, params=params, cookies=cookies, data=data)

#print(v)
print("6")

cookies=v.cookies



data = [
  ('act', 'send'),
  ('pg_code', pg_code),
  ('v_12', randint(11,59)),
  ('__backb', '0'),
  ('__no_pc', '0'),
  ('submit_button', 'Weiter'),
]
button=1

time.sleep(timer(button))
v=requests.post('https://unipark.de/#placeholder##placeholder#', headers=headers, params=params, cookies=cookies, data=data)

#print(v)
print("7")

cookies=v.cookies



data = [
  ('act', 'send'),
  ('pg_code', pg_code),
  ('v_13', ch_stand),
  ('v_14', '2'),
  ('v_15', '3'),
  ('v_16', '5'),
  ('__backb', '0'),
  ('__no_pc', '0'),
  ('submit_button', 'Weiter'),
]
button=4

time.sleep(timer(button))
v=requests.post('https://unipark.de/#placeholder##placeholder#', headers=headers, params=params, cookies=cookies, data=data)

#print(v)
print("8")

cookies=v.cookies



data = [
  ('act', 'send'),
  ('pg_code', pg_code),
  ('v_18', randint(1,2)),
  ('v_19', randint(7,32)),
  ('v_20', randint(1,8)),
  ('v_21', ''),
  ('tmp_v_21', ''),
  ('v_22', randint(1,5)),
  ('v_23', randint(1,2)),
  ('__backb', '0'),
  ('__no_pc', '0'),
  ('submit_button', 'Weiter'),
]
button=4

time.sleep(timer(button))
v=requests.post('https://unipark.de/#placeholder##placeholder#', headers=headers, params=params, cookies=cookies, data=data)

#print(v)
print("9")

cookies=v.cookies



data = [
  ('act', 'send'),
  ('pg_code', pg_code),
  ('v_24', ''),
  ('__backb', '0'),
  ('__no_pc', '0'),
  ('submit_button', 'Weiter'),
]
button=1

time.sleep(timer(button))
v=requests.post('https://unipark.de/#placeholder##placeholder#', headers=headers, params=params, cookies=cookies, data=data)

#print(v.text)
print("done")