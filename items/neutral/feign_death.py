import random

name = 'Печатка в виде черепа'

description = 'Позволяет притвориться мёртвым и выйти из любого боя.'

price = 30

usable = True
Fightable = True
disposable = True

rnd = random.random()

def on_use(user, reply):
	if rnd > 0.5:
		reply('Ты притворился мёртвым в коридоре, но зачем?')
	else:
		reply('Ты притворился мёртвым... и перестарался. Ты на самом деле умер.')
		user.death(reply, reason=name)
def fight_use(user, reply, room):
	if rnd > 0.5:
		reply('Ты притворился мёртвым и это сработало. Монстр ушёл.')
	else:
		reply('Притворясь мёртвым ты перестарался. Ты умер на самом деле.')
		user.death(reply, reason=name)	