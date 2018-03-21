# coding utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

# Импортируем модули для работы с JSON и логами.
import json
import logging
import usermanager
import config

# Импортируем подмодули Flask для запуска веб-сервиса.
from flask import Flask, request
app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)

# Хранилище данных о сессиях.
sessionStorage = {}

# Задаем параметры приложения Flask.
@app.route("/", methods=['POST'])
def main():
# Функция получает тело запроса и возвращает ответ.
    logging.info('Request %r', request.json)

    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
            "end_session": False
        }
    }

    handle_dialog(request.json, response)

    logging.info('Response %r', response)

    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )

# Функция для непосредственной обработки диалога.
def handle_dialog(req, res):
    user_id = 'alice' + req['session']['user_id']
    
    if req['session']['new']:
        # Это новый пользователь.
        # Инициализируем сессию и поприветствуем его.
        res['response']['text'] = 'Теперь скажи мне свое имя'
        usermanager.new_user(user_id)
        return
    global text, buttons_list
    text = ''
    buttons_list = [ ]

    def reply(txt, buttons=None, photo=None):
        global text, buttons_list
        text = text + '\n\n' + txt

        if buttons is None:
            return

        for btn in buttons:
            if isinstance(btn, list):
                buttons_list.extend(btn)
            else:
                buttons_list.append(btn)

    usermanager.message(user_id, reply, req['request']['command'])
    # Пользователь согласился, прощаемся.
    res['response']['text'] = text

    res['response']['buttons'] = [
        {'title': btn, 'hide': False}
        for btn in buttons_list
    ]




