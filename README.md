# Потехин Илья. ОТПРО. Лабораторная работа 3

## Установка

1. Создайте файл `.env` в корне проекта и добавьте туда ваш `ACCESS_TOKEN`:

   echo ACCESS_TOKEN=your_access_token_here > .env

2.	Установите необходимые зависимости:

    pip install -r requirements.txt

## Запуск

1. Запуск программы без аргументов выполнит запрос для пользователя с ID, установленным по умолчанию, и сохранит результат в файл `output.json`:

    python vk_fetcher.py

2. Запуск программы с аргументами:

    Если вы хотите указать пользователя ВКонтакте и файл для сохранения результатов:

    python vk_fetcher.py --user_id <ID_пользователя> --output_file <путь_к_файлу.json>

    Пример:

    python vk_fetcher.py --user_id 123456789 --output_file result.json

3. Файл результата

    {
        "user_info": {...},
        "subscriptions": {...},
        "followers": {...},
        "groups": {...}
    }
