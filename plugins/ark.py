import requests
from bs4 import BeautifulSoup
import api.api as api
import time

def main(data):
    cookies = {
        '__qca': 'I0-117545798-1669304765618',
        '_csrf': 'pBWwBB-6alrwh2JzJUwm6Ig8',
        '__qca': 'I0-117545798-1669304765618',
        '_ga': 'GA1.2.2039167498.1669203966',
        '_pbjs_userid_consent_data': '3524755945110770',
        'na-unifiedid': '%7B%22TDID%22%3A%22d8a172ab-48f8-4756-9c7e-d0309c607f6d%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-10-23T11%3A46%3A13%22%7D',
        '_gid': 'GA1.2.1274512693.1669304728',
        '__gads': 'ID=0ae7de2b0492a315:T=1669304731:S=ALNI_MZep8PAerUXVTX-s11xaWFZ-R19ew',
        '__gpi': 'UID=00000b82ff751eec:T=1669304731:RT=1669304731:S=ALNI_MYs14oJuKBHRhdIWB-r4kVP-3MKbA',
        '_csrf': '3kXhrBylskWQCGeILcq7X2iB',
        '_gat': '1',
        'cto_bundle': 'A5iXq184RnVxazFJNUN0bnRwV1FIJTJGekMlMkZYT2lxUyUyRjExblB6ZDRWZ3hPNTFxbFFCSEE3Q2c3dXBOZEJtdWxZc2lrMUpyRGFodHM0Y1BDTjR5MVp2OGlyQTVOakIzcUZuQTA4bFBhbnJMWU8yTERIbVRnTUklMkJVbmdibXpLU1lFeVRobnJ0SGRKNFp5ZXl1TDRUJTJCQTdCdEpWTWs4cjJZYkpIYlR1MURkY0xFTjMzSFRnJTNE',
    }

    headers = {
        'authority': 'www.battlemetrics.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.battlemetrics.com/servers/ark/17562863',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__qca=I0-117545798-1669304765618; _csrf=pBWwBB-6alrwh2JzJUwm6Ig8; __qca=I0-117545798-1669304765618; _ga=GA1.2.2039167498.1669203966; _pbjs_userid_consent_data=3524755945110770; na-unifiedid=%7B%22TDID%22%3A%22d8a172ab-48f8-4756-9c7e-d0309c607f6d%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-10-23T11%3A46%3A13%22%7D; _gid=GA1.2.1274512693.1669304728; __gads=ID=0ae7de2b0492a315:T=1669304731:S=ALNI_MZep8PAerUXVTX-s11xaWFZ-R19ew; __gpi=UID=00000b82ff751eec:T=1669304731:RT=1669304731:S=ALNI_MYs14oJuKBHRhdIWB-r4kVP-3MKbA; _csrf=3kXhrBylskWQCGeILcq7X2iB; _gat=1; cto_bundle=A5iXq184RnVxazFJNUN0bnRwV1FIJTJGekMlMkZYT2lxUyUyRjExblB6ZDRWZ3hPNTFxbFFCSEE3Q2c3dXBOZEJtdWxZc2lrMUpyRGFodHM0Y1BDTjR5MVp2OGlyQTVOakIzcUZuQTA4bFBhbnJMWU8yTERIbVRnTUklMkJVbmdibXpLU1lFeVRobnJ0SGRKNFp5ZXl1TDRUJTJCQTdCdEpWTWs4cjJZYkpIYlR1MURkY0xFTjMzSFRnJTNE',
    }

    response = requests.get('https://www.battlemetrics.com/servers/ark/17562863', cookies=cookies, headers=headers)
    #17562863 17503999
    #print(1)
    bsObj = BeautifulSoup(response.text, features='html.parser')

    plist=bsObj.findAll("a",{"class":"css-zwebxb"})
    ptable=bsObj.find("table",{"class":"css-1y3vvw9"}).find("tbody").findAll('tr')

    msg="当前在线玩家：\n"
    cnt=1

    for child in ptable:
        name=child.findAll('td')[0].a.get_text()
        times=child.findAll('td')[1].time.get_text()
        msg=msg+str(cnt)+"、"+name+'\t在线时长：'+times+'\n'
        cnt=cnt+1
        if cnt%15 == 0:
            api.reply_msg(data,msg)
            #print(msg)
            msg="当前在线玩家：\n"
            time.sleep(0.8)

    if cnt == 1:
        #print(msg)
        api.reply_msg(data,"当前无玩家在线")
    else:
        #print(msg)
        api.reply_msg(data,msg)
