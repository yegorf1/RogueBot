from constants import *

name = 'Кольцо'
description = (
	'… И в это кольцо он засадил всю свою жестокость,'
	'злобу свою засадил, детские комплексы,'
	'ну там привычки нехорошие и всё такое…'
)

price = 0

physical_damage = 0  # Физический урон
physical_defense = 0  # Физическая защита
magic_damage = 0  # Магический урон
magic_defense = 0  # Магическая защита

element = DEAD

for_fight = False  # Можно использовать в бою
for_use = False  # Можно использовать в коридоре
for_sale = False  # Можно продать

is_cursed = True  # проклят
is_blessed = False  # благословен


# Если для можно использовать в бою
if for_fight:
	def fight_use(user, reply, room):
		return physical_damage

# Если для можно использовать в коридоре
if for_use:
	def on_use(user, reply):
		pass

# Если можно продать - механизм продажи не реализован
# if for_sale:
# 	pass

# Если благословен
if is_cursed:
	def on_room(user, reply, room):
		reply('Опять вставило, да?')
		user.make_damage(10, 20, reply, death=False)

# Если проклят - механизм продажи не реализован
# if is_blessed:
# 	pass
