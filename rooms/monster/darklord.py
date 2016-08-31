from constants import *
import random


name = 'Темный лорд'
element = NONE
hp = 300
damage_range = (10, 12)

coins = random.randrange(0, 75, 5)

loot = ['ring']  # Кольцо


def enter(user, reply):
	reply('Кажется мы оказались не в том месте в не то время.\nОчень надеюсь что {} не обратит на нас внимание.'.format(name))

	if user.story_level < 6:
		reply('Кажется он вас не заметил.\n Вот и славненько, пойдем отсюда скорее, не будем мешать')
		user.leave(reply)

	else:
		reply('Апчих!\n Как тут пыльно!\n ОЙ! По Моему нас заметили!')