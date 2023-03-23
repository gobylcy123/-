好的，以下是一个基本的 Python 爬虫的示例，它使用 BeautifulSoup 库解析 HTML：

python
Copy code
import requests
from bs4 import BeautifulSoup

# 要爬取的网站的URL
url = 'https://www.example.com/'

# 发送 HTTP 请求
response = requests.get(url)

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 输出网站标题
print(soup.title.string)

# 输出网站的所有链接
for link in soup.find_all('a'):
    print(link.get('href'))
以上代码使用 requests 库发送 HTTP 请求，并将响应传递给 BeautifulSoup，以解析 HTML。在此示例中，我们使用 soup.title.string 输出网站标题，并使用 soup.find_all('a') 查找页面上的所有链接。