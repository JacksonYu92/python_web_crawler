import requests

res = requests.get("https://video.pearvideo.com/mp4/adshort/20200818/cont-1692368-10017283-092325_adpkg-ad_hd.mp4")

with open("yang.mp4","wb") as f:
    for item in res.iter_content():
        f.write(item)