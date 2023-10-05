import requests

url = "https://stock.xueqiu.com/v5/stock/batch/quote.json?symbol=SH000001,SZ399001,SZ399006,SH000688,SH000016,SH000300,BJ899050,HKHSI,HKHSCEI,HKHSTECH,.DJI,.IXIC,.INX"

cookie = "cookiesu=161693875396237; device_id=2e8cf6037c6a9d5d18d6ccd6a3155bbb; xq_a_token=936cf930ee4bd46499c2611037893c558c5e65ba; xqat=936cf930ee4bd46499c2611037893c558c5e65ba; xq_r_token=1acc1ba80ef30fc3ebf359cbb8714963781aa97b; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY5ODEwNzg2MSwiY3RtIjoxNjk1NjQ5NDcyOTM4LCJjaWQiOiJkOWQwbjRBWnVwIn0.faaH-JDwVY_Tqsp6PY3ZqNZBjip8C2zlJ-pXLQhGxr_S4pAQgUdG1xg3dkw2e5tSnYM3YwPIC2_6XnJAueXldtDPWkgYBgSxpLPfZ7hnG3uDPNp-JXo73caUdDWOQQzAt_4A8ognbPcIcjZsbA2o4vA5zNWQ4o2wG0JfNO-CaxMDYQ7jeLOO-Fao0tWe8yo2h9nVQRUxXJ9w5dQkDllE6Y_txDATZQQtS0RtB2CgOwGUMnfnsGdRrzI241lAsqHGaYd5OnY2x3QlkDtV21iSV36PPZV33RoPEWO84X4joxahnCvKimq5QeNVth1OFBAWQd8mEJnJ8bp7bR0eHwbI4Q; u=161693875396237; Hm_lvt_1db88642e346389874251b5a1eded6e3=1693875398,1695649478; s=c71kx6j3n4; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1696328382"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Referer": "https://xueqiu.com/",
    "cookie":cookie,
}

res = requests.get(url, headers=headers)
print(res.text)
