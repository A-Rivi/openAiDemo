

# 导入库
import requests
from bs4 import BeautifulSoup


function()
# 目标URL
url = 'https://mp.weixin.qq.com/s/KUnXlDlg-Rs_6D5RFpQbnQ'

# 发送HTTP请求获取页面内容
response = requests.get(url)

# 确保请求成功
if response.status_code == 200:
    page_content = response.content
else:
    print(f"Failed to retrieve page with status code {response.status_code}")

# 使用BeautifulSoup解析页面内容
soup = BeautifulSoup(page_content, 'html.parser')

# 选择正文内容的元素，通常微信文章的正文在一个特定的div中
article_content = soup.find('div', {'class': 'rich_media_content'})

# 提取文本内容
if article_content:
    text_content = article_content.get_text(strip=True)
    return text_content
else:
    print("Failed to find the article content.")
