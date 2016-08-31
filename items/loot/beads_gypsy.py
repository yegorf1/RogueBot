from constants import *

name = 'Бусы цыганки'
description = (
	"Если прислушатся, то можно услышать как кто-то поет"
	"*Belle*"
	"*C'est un mot qu'on...*"
)

price = 25

physical_damage = 0  # Физический урон
physical_defense = 0  # Физическая защита
magic_damage = 4  # Магический урон
magic_defense = 0  # Магическая защита

element = NONE

for_fight = False  # Можно использовать в бою
for_use = False  # Можно использовать в коридоре
for_sale = True  # Можно продать

is_cursed = False  # проклят
is_blessed = False  # благословен

# хм... фигня какая-то
mana_damage = magic_damage

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
