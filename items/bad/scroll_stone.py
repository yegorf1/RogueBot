from constants import *
import random

name = 'Свиток вызова камней'

description = (
	'Все что о нем известно, так это то что на нем нарисован камень.'
)

price = 200

fightable = True
disposable = True

def fight_use(user, reply, room):
	if user.mp >= 100:
		reply('С неба падают камни прямо на тебя и наносят 50 урона.')
		user.use_mana(50)
		user.make_damage(50, 100, reply, death=True, name='Камнепад')
		if user.hp <= 0:
			user.death(reply, reason='Камнепад')
	else:
		reply('Недостаточно маны')
		user.add_item('bad', 'scroll_stone')
	return 0