from constants import *
import random


name = 'Саламандра'
element = FIRE
hp = 75
damage_range = (10, 12)

coins = random.randrange(3, 9, 1)

loot = []
# loot = [''] Хвост саламандры


def enter(user, reply):
	reply('Вы встретили'.format(name))
