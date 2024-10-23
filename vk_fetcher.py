import requests
import json
import argparse
from dotenv import load_dotenv
import os

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получаем ACCESS_TOKEN из переменной окружения
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

DEFAULT_USER_ID = "151676573"  # ID по умолчанию
DEFAULT_OUTPUT_FILE = "output.json"  # Файл по умолчанию

# Функция для получения данных о пользователе
def get_vk_data(user_id, output_file):
    vk_api_url = "https://api.vk.com/method/"
    version = '5.131'

    # Получаем информацию о пользователе
    user_info_url = f"{vk_api_url}users.get"
    params = {
        'user_ids': user_id,
        'fields': 'followers_count',
        'access_token': ACCESS_TOKEN,
        'v': version
    }
    response_user = requests.get(user_info_url, params=params)
    user_data = response_user.json()

    # Получаем подписки пользователя (группы)
    subscriptions_url = f"{vk_api_url}users.getSubscriptions"
    params = {
        'user_id': user_id,
        'extended': 1,
        'access_token': ACCESS_TOKEN,
        'v': version
    }
    response_subs = requests.get(subscriptions_url, params=params)
    subscriptions_data = response_subs.json()

    # Получаем подписчиков пользователя (followers) с атрибутами
    followers_url = f"{vk_api_url}users.getFollowers"
    params = {
        'user_id': user_id,
        'fields': 'first_name,last_name,city,bdate',
        'access_token': ACCESS_TOKEN,
        'v': version
    }
    response_followers = requests.get(followers_url, params=params)
    followers_data = response_followers.json()

    # Получаем группы, на которые подписан пользователь
    groups_url = f"{vk_api_url}groups.get"
    params = {
        'user_id': user_id,
        'extended': 1,
        'access_token': ACCESS_TOKEN,
        'v': version
    }
    response_groups = requests.get(groups_url, params=params)
    groups_data = response_groups.json()

    # Сохраняем данные в JSON
    result = {
        'user_info': user_data,
        'subscriptions': subscriptions_data,
        'followers': followers_data,
        'groups': groups_data
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    print(f"Данные сохранены в файл {output_file}")

# Работа с аргументами командной строки
parser = argparse.ArgumentParser(description="VK API data fetcher")

# Аргументы командной строки с указанием значений по умолчанию
parser.add_argument("--user_id", default=DEFAULT_USER_ID, help="ID пользователя ВКонтакте")
parser.add_argument("--output_file", default=DEFAULT_OUTPUT_FILE, help="Путь для сохранения JSON файла")
args = parser.parse_args()

# Используем либо значения по умолчанию, либо аргументы из командной строки
user_id = args.user_id
output_file = args.output_file

# Выполняем функцию для получения данных о пользователе
get_vk_data(user_id, output_file)