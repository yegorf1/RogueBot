from constants import *

name = 'Свиток тысячи молний'

description = (
	'На свитке нарисована молния\nКажется пахнет чем-то паленым.'
)

price = 200

fightable = True
disposable = True

def fight_use(user, reply, room):
	damage_non_wet = round((user.get_damage() + user.mana_damage)/2)*1.5 + 600
	damage_wet = round((user.get_damage() + user.mana_damage)/2)*3.5 + 1800
	if user.mp < 50:
		reply('Недостаточно маны')
		user.add_item('good', 'scroll_thunderbolt')
	else:
		user.use_mana(50)
		reply('Твои руки светятся\nТы чувствуешь как по ним пробегают разряды электричества.')
		if user.wet:
			reply('Выходя из твоего тела, молния перекинулась на влажное тело и ударила тебя током.')
			user.make_damage(30, 50, reply, death=False, name='Неосторожное обращение с заклинаниями.')
		if user.wet_enemy:
			reply('Смочить врага водой было хорошей идеей.')
			return damage_wet - user.get_damage()
		else:
			return damage_non_wet - user.get_damage()
	return 0
