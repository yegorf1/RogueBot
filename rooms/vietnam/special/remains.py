import random
import usermanager
import items.itemloader as itemloader
from items.item_info import item_info

from collections import Counter

from constants import REMAINS_STICKER

name = 'Останки'

actions = [ 'Забрать себе', 'Уйти' ]

def get_actions(user):
	return actions

def enter(user, reply):
	users = list(usermanager.get_telegram_users())
	random.shuffle(users)

	user_id = None
	found_user = None

	for usr_id in users:
		usr = usermanager.get_user(usr_id)
		if usr.dead:
			user_id = usr_id
			found_user = usr
			break

	if found_user is not None:
		reply('Здесь лежат останки игрока {0}'.format(found_user.name), photo='BQADAgADFwkAAmrZzgf5q0m1CmsDggI')
		user.set_room_temp('items', found_user.items)
	else:
		reply('Здесь лежат останки лягушки. Воняет. Ты уходишь отсюда побыстрее.', photo='BQADAgADFwkAAmrZzgf5q0m1CmsDggI')
		user.leave(reply)


def action(user, reply, text):
	if text == actions[0]:
		items = [ i for i in user.get_room_temp('items', def_val=[]) if i.is_simple() ]

		if len(items) == 0:
			reply('У него ничего не было.')
		else:
			reply('Ты забрал его вещи, золотишко и парочку сохранившихся зубов.')

			user.give_gold(random.randrange(12, 72))

			user.add_item('loot', 'tooth', count=2)

			for it in items:
				user.add_item(it.group, it.name, count=it.count)

			items_str = []
			for i in items:
				loaded_item = itemloader.load_item(i.name, i.group, usr=user, count=i.count)
				if loaded_item is not None:
					items_str.append('*{0}* ({1} шт.)'.format(loaded_item.name, loaded_item.count))

			reply('Его рюкзак вмещал в себя следующие вещи: {0}'.format(', '.join(items_str)))

	else:
		reply('Ты уходишь отсюда.')
		
	user.leave(reply)
