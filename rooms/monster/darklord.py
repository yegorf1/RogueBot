from constants import *

ACTIVATED = 'activated'

actions_state_0 = ['Уходим отсюда']  # darclord passive
actions_state_1 = ['За Шир!!!', 'Сушим весла!!!']
actions_state_2 = ['Моя прелесть! МОЯ!']

name = 'Темный Лорд'
hp = 1500
damage_range = (50, 75)

coins = 0

loot = ['ring']


def get_actions(user):
	if user.get_room_temp(ACTIVATED, True):
		return user.get_fight_actions()

	else:
		if user.has_tag('nazgul_killer') and user.has_tag('shire_burned'):

			if user.has_item_tag('ring'):

				if user.has_tag('met_gollum'):
					return actions_state_0

				else:
					return actions_state_2

			else:
				return actions_state_1

		else:
			return actions_state_0


def dice(user, reply, result, subject=None):
	if result > DICE_MIDDLE:
		reply(
			'Тебе удалось!'
			'Надеюсь мы больше не встретим этого мерзкого типа!'
		)
		user.leave(reply)

	else:
		reply(
			'Не вышло!\n'
			'Ну ни чего я буду за тебя болеть!'
		)
		user.set_room_temp(ACTIVATED, True)


def enter(user, reply):
	if user.has_tag('nazgul_killer') and user.has_tag('shire_burned'):

		if user.has_item_tag('rigs'):

			if user.has_tag('met_gollum'):

				reply('Темный Лорд исчез')

			else:

				hp = 3000

				user.remove_item('rigs')  # У игрока должно быть только одно кольцо!
				reply(
					'«_Я чувстую его! Оно мое!_»\n\n'
					'Мамочки! Мне страшно!\n'
					'Верни ему то что он просит! НЕМЕДЛЕННО!'
				)

		else:
			reply(
				'Темный Лорд медленно поворачивается и замечает незваного гостя\n\n'
				'Мамочки! что сейчас будет!!!'
			)

	else:
		reply(
			'Кажется мы оказались не в том месте в не то время.\n'
			'Очень надеюсь что {} не обратит на нас внимание.'.format(name)
		)

		user.set_room_temp(ACTIVATED, False)


def action(user, reply, text):
	if user.get_room_temp(ACTIVATED, True):
		user.fight_action(reply, text)

	else:

		if user.has_tag('nazgul_killer') and user.has_tag('shire_burned'):

			if user.has_item_tag('rigs'):

				if user.has_tag('met_gollum'):

					if text == actions_state_0[0]:
						user.leave(reply)

			else:
				# Кольцо
				if text == actions_state_2[0]:
					user.set_room_temp(ACTIVATED, True)

		else:
			# Назгулы
			if text == actions_state_1[0]:
				user.set_room_temp(ACTIVATED, True)

			else:
				reply('Кидай кубики')
				user.throw_dice(reply)

	user.leave(reply)
