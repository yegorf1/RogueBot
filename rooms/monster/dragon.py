from constants import *

name = 'Дракон'

hp = 100
element = NONE
damage_range = ( 15, 30 )

coins = 300

loot = [ 'dragon_sword' ]

def enter(user, reply):
	reply('Большой и красный, как в сказке')

	if user.story_level < 1:
		reply('Он не заметил тебя и прошел мимо. Мелкий еще.')
		user.leave(reply)
