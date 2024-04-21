from requests_html import HTMLSession

'''
for div class searching do "div. "
for span class do "span. "
for span id do "span# "

'''


session = HTMLSession()

city = 'phoenix'
st = 'az'
url = f'https://www.google.com/search?q=weather+{city}+{st}'


r = session.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})


temperature = r.html.find('span#wob_tm', first=True).text
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
condition = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text

print(temperature, unit, condition)




