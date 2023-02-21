import requests
import json
import os
import mtranslate



# if not os.path.exists('D:\\gitPush\json\Gitpush'):
#     os.makedirs('D:\\gitPush\json\Gitpush')
# theme1 = 'Политика'
# theme2 = 'Технология'
# apiKey = '8f29e197997d45379ad115dbf0dedfc8'
#
# url = ('https://newsapi.org/v2/everything?q=' + theme1 + '&apiKey=' + apiKey)
#
# response = requests.get(url)
#
# data = response.json()
#
# with open('D:\\gitPush\\json\\Gitpush\\polit.json', 'w', encoding='utf-8') as file:
#     json.dump(data, file, ensure_ascii=False, indent=4)
#
# url2 = ('https://newsapi.org/v2/everything?q=' + theme2 + '&apiKey=' + apiKey)
#
# response = requests.get(url2)
#
# data2 = response.json()
#
# with open('D:\\gitPush\\json\\Gitpush\\tech.json', 'w', encoding='utf-8') as file:
#     json.dump(data2, file, ensure_ascii=False, indent=4)


# apiKey = '[8f29e197997d45379ad115dbf0dedfc8]'
# url = ('https://newsapi.org/v2/everything?q=' + theme + '&apiKey=' + apiKey)

theme = 'world'
api = "NTRPl05Akxo5IzRMEPM1nsJVZQQH7xN5"
url = 'https://api.nytimes.com/svc/topstories/v2/' + theme + '.json?api-key=' + api


# response = requests.get(url)
# data = json.loads(response.text)
# articles = data['results']
#
# resultRus = []
#
# for article in articles:
#     title_rus = mtranslate.translate(article['title'], 'ru', 'en')
#     desc_rus = mtranslate.translate(article['abstract'], 'ru', 'en')
#     link = article['url']
#     image = article['multimedia'][0]['url']
#     resultRus.append({'title': title_rus, 'description': desc_rus, 'link': link, 'image': image})
#
# with open('C:/json/data.json', 'w', encoding='utf-8') as f:
#     json.dump(resultRus, f, ensure_ascii=False)
#
# # Выводим заголовок и описание первой новости на экран
# print(resultRus[2]['title'])
# print(resultRus[2]['description'])
num = 19
with open('C:/json/data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
with open('D:/gitPush/json/Gitpush/tech.json', 'r', encoding='utf-8') as f:
    data2 = json.load(f)
print(data[num]['title'])
print(data[num]['description'])