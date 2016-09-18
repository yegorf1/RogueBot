from constants import *
import user.stats_defenition as stats_defenition
import random

name = 'Водяной свиток (20mp)'

description = (
	'Свиток мокрый\nТы попробовал его выжать, но он снова стал мокрым'
)


price = 100

fightable = True
disposable = True

def fight_use(user, reply, room):
	if user.mp >= 20:
		reply('Вместо крови по твоим жилам идет вода!\nТы указываешь руками на врага и его обливает водой!')
		user.use_mana(20)
		user.wet_enemy = True
		if random.random() < 0.1:
			user.wet = True
			reply('К сожалению на брызги разлетелись во все стороны и ты тоже стал мокрым')
		return 100 - stats_defenition.get_damage(user)
	else:
		reply('Недостаточно маны')
		user.add_item('good', 'scroll_water')
		return 0
