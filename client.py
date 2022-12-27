import requests
res = requests.post('http://localhost:5000/', json={"url":"https://listiyo.com/img/anasayfa/16.png", "type":"convert", "width":"400"})
if res.ok:
    print(res.json())