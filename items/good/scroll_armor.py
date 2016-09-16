from constants import *
import random

name = 'Свиток: железный панцирь (50mp)'

description = (
	'Свиток железный, его не согнуть'
)

price = 100

fightable = True
disposable = True

def fight_use(user, reply, room):
	if user.used_armor == False:
		if user.mp >= 50:
			reply('Ты читаешь заклинание и твои руки начинают трястись.\nТы не в состоянии их больше сдерживать\nОни начинают описывать круги. Твоя броня увеличилась на 1000 очков')
			user.mp -= 50
			user.defence += 1000
			user.used_armor = True
		else:
			reply('Недостаточно маны')
	else:
		reply('Ты уже использовал это заклинание')
	return 0
