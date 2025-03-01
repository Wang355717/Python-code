import requests
from bs4 import BeautifulSoup

# 网址 https://bidding.sinopec.com/tpfront/xxgg/004005/?Paging=1

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
response = requests.get('https://bidding.sinopec.com/tpfront/xxgg/004005/', headers=header)
soup = BeautifulSoup(response.text, 'lxml')

for i, a in enumerate(soup.select('a.WebList_sub')):
    print('https://bidding.sinopec.com' + a['href'])
    response = requests.get('https://bidding.sinopec.com' + a['href'], headers=header)
    soup = BeautifulSoup(response.text, 'lxml')
    element = soup.select('table#filedown a')

    if len(element) > 0:
        pdf_url = element[0]['href']
        response = requests.get(pdf_url, headers=header)
        with open(f'{i}.pdf', 'wb') as f:
            f.write(response.content)
