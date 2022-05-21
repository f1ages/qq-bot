import api.api as api
import requests
import json
from config import xcx_coingroup

def check(id):
    if id=='LUNA':
        return '561'
    elif id=='USDC':
        return '678'
    elif id=='OSMO':
        return '1'
    else:
        return False

def get_price(id1,id2):
    url_id1="https://lcd-osmosis.keplr.app/osmosis/gamm/v1beta1/pools/"+id1
    url_id2="https://lcd-osmosis.keplr.app/osmosis/gamm/v1beta1/pools/"+id2

    try:
        id1_html=requests.get(url_id1)
        id2_html=requests.get(url_id2)
    except:
        return False

    id1_json=json.loads(id1_html.text)
    id2_json=json.loads(id2_html.text)

    id1_amount=float(id1_json['pool']['poolAssets'][0]['token']['amount'])
    id1_uosmo_amount=float(id1_json['pool']['poolAssets'][1]['token']['amount'])
    id2_amount=float(id2_json['pool']['poolAssets'][0]['token']['amount'])
    id2_uosmo_amount=float(id2_json['pool']['poolAssets'][1]['token']['amount'])

    id1_uosmo_price=id1_amount/id1_uosmo_amount
    id2_uosmo_price=id2_amount/id2_uosmo_amount

    id1_id2=id2_uosmo_price/id1_uosmo_price

    return id1_id2

def main(data):

    id1=check(str(data['message'])[1:5])
    id2=check(str(data['message'])[5:9])
    if id1==False or id2==False:
        api.reply_msg(data,'no such coin')
        return
    else:
        pri=get_price(id1,id2)
        if pri==False:
            api.reply_msg(data,'network err')
        else:
            api.reply_msg(data,'osmo: '+str('%.10f' %pri)+'\n'+'币安：network err')


