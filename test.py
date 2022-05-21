import requests

headers = {
    'authority': 'api.uniswap.org',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '*/*',
    'origin': 'https://app.uniswap.org',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://app.uniswap.org/',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

params = {
    'protocols': 'v2,v3',
    'tokenInAddress': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
    'tokenInChainId': '1',
    'tokenOutAddress': '0xdAC17F958D2ee523a2206206994597C13D831ec7',
    'tokenOutChainId': '1',
    'amount': '1000000000000000000',
    'type': 'exactIn',
}

response = requests.get('https://api.uniswap.org/v1/quote', params=params, headers=headers)
print(response.text)