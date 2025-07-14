from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
from datetime import datetime

def get_cookies_with_selenium(url):
    """
    使用selenium获取完整的cookies
    """
    options = Options()
    options.add_argument('--headless')  # 无头模式，可选
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(url)
        time.sleep(3)  # 等待页面加载完成
        cookies = driver.get_cookies()
        return cookies
    finally:
        driver.quit()
        
def save_cookies_to_netscape(cookies, filename="cookies.txt"):
    """
    将cookies保存为Netscape格式
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Netscape HTTP Cookie File\n")
        f.write("# http://curl.haxx.se/rfc/cookie_spec.html\n")
        f.write("# This is a generated file!  Do not edit.\n\n")
        
        for cookie in cookies:
            # 格式：domain flag path secure expiry name value
            domain = cookie.get('domain', '')
            flag = 'TRUE' if domain.startswith('.') else 'FALSE'
            path = cookie.get('path', '/')
            secure = 'TRUE' if cookie.get('secure', False) else 'FALSE'
            expiry = str(int(cookie.get('expiry', 0))) if cookie.get('expiry') else '0'
            name = cookie.get('name', '')
            value = cookie.get('value', '')
            
            line = f"{domain}\t{flag}\t{path}\t{secure}\t{expiry}\t{name}\t{value}\n"
            f.write(line)


if __name__ == '__main__':
    print("请输入url:")
    url = input()
    print("请输入cookies文件名（默认：cookies.txt）:")
    filename = input().strip() or "cookies.txt"
    
    cookies = get_cookies_with_selenium(url)
    save_cookies_to_netscape(cookies, filename)
    print(f"成功导出 {len(cookies)} 个cookies到 {filename}")


