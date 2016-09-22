name = 'Записка'
price = 1
description = 'Какой-то комок бумаги.'

usable = True

def on_use(user, reply):
	stealer = user.get_variable('stealer', 'none')
	stolen_item = user.get_variable('stolen_item', 'none')

	thought = 'Кто же это мог быть..'
	if stealer != 'none':
		thought = 'Судя по почерку это мог быть только {0}! Ты лишился {1}.'.format(stealer, stolen_item)

	reply('Ты развернул комок бумаги прочитал:')
	reply('«Ахаха! Тебя обокрали!»\n{0}'.format(thought))