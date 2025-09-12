import requests

url = 'https://www.hupu.com/'

params = {
    'c': 'a',
    'encode': 'json'
}

try:
    print(f"正在发送 GET 请求到:{url},参数:{params}")
    responses = requests.get(url, params=params)
    status_code = responses.status_code
    if status_code == 200:
        print(f"请求成功 状态码:{status_code}")
        # 获取整个网页内容
        html_content = responses.text

        # 打印网页全部内容
        print(html_content)

        # 也可以保存到文件，方便在浏览器打开
        with open("hupu.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        print("网页内容已保存到 hupu.html")
    else:
        print(f"请求失败,状态码:{status_code}")
except requests.RequestException as e:
    print(f"请求异常:{e}")
