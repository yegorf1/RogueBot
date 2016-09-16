from constants import *
import user.stats_defenition as stats_defenition

name = 'Свиток: удар молнии (50mp)'

description = (
	'На свитке нарисована молния\nКажется пахнет чем-то паленым'
)

price = 200

fightable = True
disposable = True

def fight_use(user, reply, room):
	damage_non_wet = round((user.damage + user.mana_damage)/2)*1.5 + 600
	damage_wet = round((user.damage + user.mana_damage)/2)*3.5 + 1800
	if user.mp < 50:
		reply('Недостаточно маны')
	else:
		user.mp -= 50
		reply('Твои руки светятся\nТы чувствуешь как по ним пробегают разряды электричества')
		if user.wet:
			reply('Выходя из твоего тела, молния перекинулась на влажное тело и ударила тебя током')
			if user.hp > 30:
				user.hp -= 30
			else:
				user.hp -= round(0.9*user.hp)
		if user.wet_enemy:
			reply('Смочить врага водой было хорошей идеей')
			return damage_wet - stats_defenition.get_damage(user)
		else:
			return damage_non_wet - stats_defenition.get_damage(user)
	return 0