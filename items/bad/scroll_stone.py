from constants import *
import random

name = 'Свиток: камень(100mp)'

description = (
	'Все что о нем известно, так это то что на нем нарисован камень'
)

price = 200

fightable = True
disposable = True

def fight_use(user, reply, room):
	if user.mp >= 100:
		reply('С неба падают камни прямо на тебя и наносят 50 урона')
		user.mp -= 100
		user.hp -= 50
		if user.hp <= 0:
			user.death(reply, reason='Камнепад')
	else:
		reply('Недостаточно маны')
	return 0
