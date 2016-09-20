from constants import *
import random

name = 'Свиток черепахи'

description = (
	'Свиток железный, его не согнуть'
)

price = 100

fightable = True
disposable = True

def fight_use(user, reply, room):
	if user.used_armor == False:
		if user.mp >= 50:
			reply('Ты читаешь заклинание и твои руки начинают трястись.\nТы не в состоянии их больше сдерживать\nОни начинают описывать круги. Твоя броня увеличилась на 1000 очков.')
			user.use_mana(50)
			user.defence += 1000
			user.used_armor = True
		else:
			reply('Недостаточно маны')
			user.add_item('good', 'scroll_armor')
	else:
		reply('Ты уже использовал это заклинание')
		user.add_item('good', 'scroll_armor')
	return 0
