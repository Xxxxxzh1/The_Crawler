#!/usr/local/bin/python3

import re
import requests

response = requests.get('http://www.ku6.com/index')
result_list = re.findall('<a class="video-image-warp" target="_blank" href="(.*?)">', response.text)
count = 0

for result in result_list:

    if result.startswith('/video'):
        result = f"http://www.ku6.com{result}"

        "把所有组合好的url写入文件"
        with open('./video_onku6/video_list.txt', 'a+') as list:
            list.write(result + '\n')

        result_data = requests.get(result)
        video_data = result_data.text
        video_url = re.findall('flvURL: "(.*?)"', video_data)
        video_response = requests.get(video_url[0])
        video_bytes = video_response.content
        with open(f"./video_onku6/{count}_video.mp4", "wb") as fw:
            fw.write(video_bytes)
            fw.flush()
            print('%d_video success download' % (count))
            count += 1

print("爬虫结束")
