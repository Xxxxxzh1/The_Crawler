#!/usr/local/bin/python3

import requests
# import re

# 实例化session对象
new_session = requests.session()
# 登陆请求url
login_url = 'http://pan.zerozero.cn:88/index.php/login'
# 网盘文件主页
file_url = 'http://pan.zerozero.cn:88/index.php/apps/files/'

# 设置请求头
req_header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'oc_sessionPassphrase=bnbDYGkMbX7YUbVid2uAyQ7l%2BZdNB56Sf1QEjdCwzZrf6CFxhLOWOJ39MtkJaUo2lcW2upgC2Gj7Yoabei62u93HT7B%2Bb0S%2F6Hbv2uAY2fZV%2FH2eDjIbI%2FnOP4IyJKbz; oc8uf1v5g5wi=7546dac9d226abc3f07f4856d9820d26',
    'Host': 'pan.zerozero.cn:88',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}

# 设置登陆表单
from_data = {
    'user': 'zhengzhi',
    'password': '00@12345',
    'remember_login': '1',
    'timezone-offset': '8',
    'timezone': 'Asia/Shanghai',
    'requesttoken': 'MhkTAmIUFAoYdhoOMURzEwkMcnIFHzIFGiEJPjd1Qj0=:hzPLSEff70NVW+CTPDYFnvC0Vh8qV9qkmcSh7txaWDg='
}

if(new_session.get(login_url).status_code == 200):
    print('网盘服务器连接成功')
    login_res = new_session.post(file_url, headers=req_header)
    print(login_res.status_code)

else:
    print(new_session.post(login_url).status_code)
