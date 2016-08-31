from constants import *
import random


name = 'Миньон'
element = NONE
hp = 23
damage_range = (1, 4)

coins = random.randrange(5, 10, 2)

loot = ['banana']  # Слезы Наяды


def enter(user, reply):
	reply('Вы встретили'.format(name))