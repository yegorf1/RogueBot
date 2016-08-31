from constants import *
import random


name = 'Наяда'
element = WATER
hp = 30
damage_range = (3, 7)

coins = random.randrange(7, 9, 1)

loot = []
# loot = [''] Слезы Наяды


def enter(user, reply):
	reply('Вы встретили'.format(name))