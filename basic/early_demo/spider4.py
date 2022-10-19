import  requests
response = requests.get('http://i3.1100lu.xyz/vod/2017-08-09/5989f0eac8cd5.jpg')
with open('neizi.jpg','wb') as f:
    f.write(response.content)