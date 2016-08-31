from constants import *
import random


name = 'Горгулья'
element = NONE
hp = 35
damage_range = (5, 9)

coins = random.randrange(10, 15, 1)

loot = ['beads_gypsy']  # Бусы цыганки


def enter(user, reply):
	reply('Вы встретили'.format(name))