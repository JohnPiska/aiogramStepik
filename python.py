import requests
import time

api_url = 'https://api.telegram.org/bot'
api_cats_url = 'https://random.dog/woof.json'
bot_token = ''
error_text = 'ОШИБКА'
max_counter = 100

offset = -2
counter = 0
cat_response: requests.Response
cat_link: str

while counter < max_counter:

    print('attempt =', counter)

    updates = requests.get(f'{api_url}{bot_token}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(api_cats_url)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                requests.get(f'{api_url}{bot_token}/sendPhoto?chat_id={chat_id}&phot={cat_link}')
            else:
                requests.get(f'{api_url}{bot_token}/sendPhoto?chat_id={chat_id}&phot={error_text}')

    time.sleep(1)
    counter += 1