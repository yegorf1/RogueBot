from constants import *
from random import randrange

FIGHT = 'За Шир!!!'
ESCAPE = 'Попытаться убежать'

name = 'Темный лорд'
hp = 1000  # Темный Лорд должен быть лютым парнем! А то что-то они там все перекаченные какие-то
damage_range = ( 20, 25 )

coins = randrange(200, 400, 10)

loot = [ 'ring' ]


def enter(user, reply):
	reply(
		'Кажется мы оказались не в том месте в не то время.\n'
		'Очень надеюсь что {} не обратит на нас внимание.'.format(name)
	)

	if user.darklord_level < 25:
		reply(
			'Кажется он вас не заметил.\n'
			'Вот и славненько, пойдем отсюда скорее, не будем мешать'
		)
		user.leave(reply)

	else:

		if not user.has_item('rigs'):
			reply(
				'Апчих!\n'
				'Как тут пыльно!\n'
				'ОЙ! По Моему нас заметили!'
			)

		else:
			user.remove_item('rigs')  # У игрока должно быть только одно кольцо!
			reply(
				'«_Я чувстую его! Оно мое!_»\n'
				'Мамочки! Мне страшно!\n'
				'Верни ему то что он просит! НЕМЕДЛЕННО!'
			)

		user.user.set_room_temp('question')


def dice(user, reply, result, subject=None):

	if subject == ESCAPE:

		if result > DICE_MIDDLE:
			reply('Тебе удалось! Надеюсь мы больше не встретим этого мерзкого типа!')
			user.leave(reply)

		else:
			reply('ОЙ! Как смешно лопнула твоя голова!')
			user.death(reply)


def action(user, reply, text):
	question = user.get_room_temp('question')

	if text == FIGHT:
		# Тут нужно запустить обычный бой с монстром
		pass

	elif text == ESCAPE:
		reply(
			'«_Апчих! Пора тут прибарться_»\n'
			'Кидай кубики, это наш шанс!!!'
		)
		user.throw_dice(reply, ESCAPE)


def get_actions(user):
	question = user.get_room_temp('question')
	return [FIGHT, ESCAPE]
