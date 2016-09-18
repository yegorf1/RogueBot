from constants import *
import user.stats_defenition as stats_defenition
import random

name = 'Супер свиток (100mp)'

description = (
	'Только лишь взглянув на него, твои мускулы увеличились. Ты хочешь кого-то ударить'
)

price = 500

fightable = True
disposable = True

def fight_use(user, reply, room):
	if user.mp >= 100:
		reply('Твои руки увеличиваются и ты со всей силы бьешь врагу в лицо!')
		user.use_mana(100)
		return stats_defenition.get_damage(user)*3
	else:
		reply('Недостаточно маны')
		user.add_item('good', 'scroll_superpower')
		return 0
