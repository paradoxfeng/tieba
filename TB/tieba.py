import requests
import re

r = requests.get('https://tieba.baidu.com/p/3138733512?see_lz=1&pn=1').text
#print(r)
pattern = re.compile('<h3 class="core_title_txt pull-left text-overflow  " title="(.*?)" style',re.S)
title = re.search(pattern,r).group(1)
#print(title)
pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
contents = re.findall(pattern,r)
for x in contents:
    removeImg = re.compile('<img.*?>| {7}|')
    x = re.sub(removeImg, "", x)
    removeAddr = re.compile('<a.*?>|</a>')
    x = re.sub(removeAddr, "", x)
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    x = re.sub(replaceLine, "\n", x)
    replaceTD = re.compile('<td>')
    x = re.sub(replaceTD, "\t", x)
    replacePara = re.compile('<p.*?>')
    x = re.sub(replacePara, "\n    ", x)
    replaceBR = re.compile('<br><br>|<br>')
    x = re.sub(replaceBR, "\n", x)
    removeExtraTag = re.compile('<.*?>')
    x = re.sub(removeExtraTag, "", x)
    print(x.strip())
    print('---------------------------------------------------------------------')
    with open('tb.txt','a') as f:
        f.write(x)

