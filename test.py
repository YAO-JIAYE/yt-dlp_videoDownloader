import requests

# 添加用户代理以模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get("https://www.bilibili.com/video/BV1sg411Y7n7/?spm_id_from=333.337.search-card.all.click&vd_source=8d3ddbf2d0edec4feaea7e750337df94", headers=headers)
print(response.cookies)

