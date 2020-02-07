#!/usr/local/bin/python3

import re
import requests

user_id = '124754760'

# 实例化的session对象
new_session = requests.session()

# 登陆请求URL
main_url = 'https://www.douban.com/'
# 个人主页URL
account_url = 'https://www.douban.com/people/124754760/'

# 设置请求头
req_header = {
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}

# 设置cookies
cookies = {
    'cookie': 'bid=-QEr7ipHyMk; douban-fav-remind=1; __utmc=30149280; __gads=ID=9d25da31400b2a61:T=1580562513:S=ALNI_MblNCY1v1ctX0AFqQCim7zFzHajWQ; push_noty_num=0; push_doumail_num=0; __utmv=30149280.12475; __yadk_uid=cdvOu4FoYe2Mx5RtgJjXPgttFO7HC669; douban-profile-remind=1; __utmz=30149280.1580806470.4.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; ll="118259"; ps=y; dbcl2="124754760:5LdGHllHOvE"; ck=BLJS; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1580822283%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%22%5D; _pk_id.100001.8cb4=58fecc4cf6373846.1580562512.6.1580822283.1580814363.; _pk_ses.100001.8cb4=*; ap_v=0,6.0; __utma=30149280.2096454760.1580562513.1580813792.1580822293.6; __utmt=1; __utmb=30149280.2.10.1580822293'
}

# 设置登陆表单
from_data = {
    'name': '17551018764',  # 账号
    'password': 'zz1111111',  # 密码
    'remember': 'true'  # 记住当前登陆信息
    # 'ticket': 'mMYwAI2-OqXLYhyCsF9S8C1yT758gJnfvsxaTFwPYZjZP2zZKqygcjHS5fg5JN-LowYzE-Hp0U4*'  # 图形验证码
}

response = new_session.post(main_url, headers=req_header, cookies=cookies)

# 正则匹配返回状态
regex_status = re.compile(r'data-uid="(.*?)"')
result = regex_status.findall(response.text)

if (user_id in result):
    print("登陆成功")
else:
    print("登陆失败")
