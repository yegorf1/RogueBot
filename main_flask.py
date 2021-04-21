from flask import Flask, abort, jsonify, request
from collections import deque
from functools import wraps
import time
import usermanager

queue = {}

app = Flask(__name__)


def validate_token(func):
    @wraps(func)
    def wrapped(token):
        uid, token = token.split(':')
        uid = int(uid)
        usr = usermanager.get_user(uid)
        if usr is None:
            return abort(403)
        if usr.get_bot_token() != token:
            return abort(403)
        return func(uid, usr)
    return wrapped


@app.route('/api/<token>/send', methods=['POST', 'GET'])
@validate_token
def send_message(uid, usr):
    msg = request.values.get('message', None)
    if msg is None:
        return abort(400)
    usermanager.message(uid, lambda *a, **k: reply(uid, *a, **k), msg)
    return jsonify({'ok': True})


@app.route('/api/<token>/messages', methods=['GET'])
@validate_token
def get_messages(uid, usr):
    if request.values.get('clear', False):
        messages = list(queue.pop(uid, []))
    else:
        messages = list(queue.get(uid, []))
    return jsonify(messages)


@app.route('/api/<token>/cheat_stats')
@validate_token
def cheat_stats(uid, usr):
    params = {
            'hp': 0,
            'mp': 0,
            'gold': 0,
            'max_hp': 0,
            'max_mp': 0,
            'damage': 0,
            'defence': 0,
            'charisma': 0,
            'mana_damage': 0
    }
    for key in params.keys():
        params[key] = getattr(usr, key)
    zero = request.values.get('zero', False)
    for key in params.keys():
        val = int(request.values.get(key, 0))
        if val != 0:
            if zero:
                params[key] = val
            else:
                params[key] += val
            setattr(usr, key, params[key])
    usr.cheater = True
    usermanager.save_user(usr)
    return jsonify(params)


def reply(uid, txt=None, buttons=None, photo=None):
    if uid not in queue:
        queue[uid] = deque(maxlen=100)
    queue[uid].append({
        'text': txt,
        'buttons': buttons,
        'sticker': photo,
        'time': time.time()
    })


if __name__ == "__main__":
    app.run(port=32000)

