from constants import *

# Снимает одно случайное прокляьте
name = 'Слезы Наяды'
description = (
	'Кап-Кап-Кап'
	'Из ясных глаз'
)

price = 50

physical_damage = 0  # Физический урон
physical_defense = 0  # Физическая защита
magic_damage = 0  # Магический урон
magic_defense = 0  # Магическая защита

element = NONE

for_fight = False  # Можно использовать в бою
for_use = True  # Можно использовать в коридоре
for_sale = True  # Можно продать

is_cursed = False  # проклят
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

# Если благословен - механизм продажи не реализован
# if is_cursed:
# 	pass

# Если проклят - механизм продажи не реализован
# if is_cursed:
# 	pass
