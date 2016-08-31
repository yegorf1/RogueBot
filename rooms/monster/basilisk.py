from constants import *
import random


name = 'Василиск'
element = NONE
hp = 150
damage_range = (17, 20)

coins = random.randrange(14, 21, 1)

loot = []
loot = ['tooth_basilisk']  # Зуб Василиска


def enter(user, reply):
	reply('Вы встретили'.format(name))