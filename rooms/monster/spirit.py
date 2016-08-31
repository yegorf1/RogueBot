from constants import *
import random


name = 'Дух бесплотный'
element = DEAD
hp = 10
damage_range = (1, 5)

coins = 0

loot = []


def enter(user, reply):
	reply('Вы встретили'.format(name))