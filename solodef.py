import telebot
import json

def get_cfg():
    with open('bot.cfg', 'r', encoding='utf-8') as f:
        config = json.load(f)
        return config


def get_token():
    url = 'https://api.moyklass.com/v1/company/auth/getToken'
    apiKey = get_cfg()['Ключ API CRM системы']
    apiKey = {"apiKey": apiKey}
    response = requests.post(url, json=apiKey, timeout=60)
    json_str = response.json()
    token = json_str['accessToken']
    header = {'x-access-token': token}
    return header


def get_user_list():
    header = get_token()
    url = 'https://api.moyklass.com/v1/company/users'
    response = requests.get(url, headers=header, timeout=60)
    user_list = []
    for i in response.json()['users']:
        a = i['phone'][0] + i['phone'][1] + i['phone'][2]
        if i['phone'][0] != '7' and a != '374':
            for j in i['phone']:
                if j != '1':
                    a = [i['name'], i['phone'], i['id']]
                    user_list.append(a)
                    break
        if i['phone'] == '':
            user_list.append(a)
    return user_list


def replace_number(userId):
    header = get_token()
    userId = int(userId)
    url_get = f'https://api.moyklass.com/v1/company/users/{userId}'
    response = requests.get(url_get, headers=header, timeout=60)
    user_data = response.json()
    print("Текущие данные:", user_data)
    updated_data = user_data.copy()
    read_only_fields = ['id', 'userId', 'createdAt', 'updatedAt', 'createdBy', 'balans', 'bonusBalance', 'availableBalance', 'stateChangedAt', 'joins', 'tags', 'createSourceId']
    for field in read_only_fields:
        if field in updated_data:
            del updated_data[field]
    if 'attributes' in updated_data and isinstance(updated_data['attributes'], list):
        for attribute in updated_data['attributes']:
            if isinstance(attribute, dict):
                if 'attributeAlias' in attribute:
                    del attribute['attributeAlias']
                if 'attributeName' in attribute:
                    del attribute['attributeName']
                if 'attributeType' in attribute:
                    del attribute['attributeType']
    updated_data['phone'] = '1111111111'
    url = f'https://api.moyklass.com/v1/company/users/{userId}'
    update_response = requests.post(url, headers=header, json=updated_data, timeout=60)
    print(update_response.json())



