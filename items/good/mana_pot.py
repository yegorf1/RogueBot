from constants import *

name = 'Светящееся зелье'

description = (
	'В пробирке плавает чистая энергия'
)

price = 100

usable = True
disposable = True

def on_use(user, reply):
	reply('Это оказалось зелье маны. Она польностью восстановилась')

	user.mp = user.max_mp

fightable = True
def fight_use(user, reply, room):
	on_use(user, reply)

	return 0
