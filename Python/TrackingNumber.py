from bs4 import BeautifulSoup
import mechanize

mc = mechanize.Browser()
mc.set_handle_robots (False)

url = 'https://www.findandtrace.com/trace-mobile-number-location'
mc.open(url)

mc.select_form(name='trace')
mc ['mobilenumber'] = '+989039851230'
res = mc.submit().read()

soup = BeautifulSoup (res, 'html.parser')
tbl = soup.find_all('table',class_='shop_table')

data = tbl[0].find('tfoot')
c=0

for i in data:
    c += 1
    if c in (1,4,6,8):
        continue
    th = i.find('th')
    td = i.find('td')
    print(th. text, td. text)
