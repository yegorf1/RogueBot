from constants import *
import random


name = 'Голем'
element = STONE
hp = 250
damage_range = (20, 25)

coins = random.randrange(40, 90, 10)

loot = ['stone_heart']  # Каменное сердце


def enter(user, reply):
	reply('Вы встретили'.format(name))