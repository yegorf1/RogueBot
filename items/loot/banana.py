from constants import *

name = 'Банан'
description = (
	'Обычный спелый банан'
)

price = 2

physical_damage = 0  # Физический урон
physical_defense = 0  # Физическая защита
magic_damage = 0  # Магический урон
magic_defense = 0  # Магическая защита

element = NONE

for_fight = True  # Можно использовать в бою
for_use = True  # Можно использовать в коридоре
for_sale = True  # Можно продать

is_cursed = False  # проклят
is_blessed = False  # благословен


# Если для можно использовать в бою
if for_fight:
	def fight_use(user, reply, room):
		if room.code_name == 'minion':
			reply('С криками "BANANA!" миньон скрылся в неизвестно направлении')
			user.won(reply)

			return 0
		else:
			reply('Ты поскользнулся на кожуре\Теперь будет синяк')
			user.make_damage(1, 2, reply, death=False)
			return 0

# Если для можно использовать в коридоре
if for_use:
	def on_use(user, reply):
		reply('Ты чувствуешь себя лучше, теперь главное не поскользнуться на кожуре')

		user.hp += 15

# Если можно продать - механизм продажи не реализован
# if for_sale:
# 	pass

# Если благословен - механизм продажи не реализован
# if is_cursed:
# 	pass

# Если проклят - механизм продажи не реализован
# if is_cursed:
# 	pass
