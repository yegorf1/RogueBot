from constants import *
import random


name = 'Водяной'
element = WATER
hp = 45
damage_range = (6, 12)

coins = random.randrange(15, 30, 1)

loot = ['drawing_flying_ship'] # Чертеж летучего корабля


def enter(user, reply):
	reply('Вы встретили'.format(name))