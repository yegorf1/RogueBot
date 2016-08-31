from constants import *
import random


name = 'Зобми'
element = DEAD
hp = 20
damage_range = (0, 2)

coins = random.randrange(0, 5, 1)

loot = ['dentures']  # Вставная челюсть


def enter(user, reply):
	reply('Вы встретили'.format(name))