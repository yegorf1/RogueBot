from constants import *
import random


name = 'Сильфида'
element = NONE
hp = 25
damage_range = (7, 14)

coins = random.randrange(12, 18, 2)

loot = ['ballet_tutu']  # Балетная пачка


def enter(user, reply):
	reply('Вы встретили'.format(name))