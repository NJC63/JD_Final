from requests_html import HTMLSession

'''
for div class searching do "div. "
for span class do "span. "
for span id do "span# "

'''


session = HTMLSession()

city = 'atlanta'
st = 'ga'
url = f'https://www.google.com/search?q=weather+{city}+{st}'


r = session.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})

# Current weather conditions
temperature = r.html.find('span#wob_tm', first=True).text
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
condition = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text

precipitation = r.html.find('div.wtsRwe', first=True).find('span#wob_pp', first=True).text
humidity = r.html.find('div.wtsRwe', first=True).find('span#wob_hm', first=True).text
wind = r.html.find('div.wtsRwe', first=True).find('span#wob_ws', first=True).text


print(temperature, unit, condition)

# Weeks forecast

forecast = r.html.find('div.wob_dfc', first=True).find('div.wob_df')
daysOfWeek, highTemps, lowTemps, conditions = [], [], [], []

i = 0
while(i < len(forecast)):
    day = forecast[i].find('div.Z1VzSb', first=True)
    daysOfWeek.append(day.text)

    high = forecast[i].find('div.gNCp2e span.wob_t', first=True)
    highTemps.append(high.text)

    low = forecast[i].find('div.QrNVmd.ZXCv8e span.wob_t', first=True)
    lowTemps.append(low.text)

    condition = forecast[i].find('img.YQ4gaf.zr758c', first=True)
    conditions.append(condition.attrs['alt'])

    i += 1

print(daysOfWeek)
print(highTemps)
print(lowTemps)
print(conditions)




