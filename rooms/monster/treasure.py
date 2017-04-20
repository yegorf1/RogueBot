from constants import *

name = 'Сокровищница'

hp = 10
damage_range = ( 50, 50 )
loot = [ ]

UP = 'NEVER GONNA GIVE YOU UP!'
DOWN = 'NEVER GONNA LET YOU DOWN!'
AROUND = 'NEVER GONNA RUN AROUND!'
DESERT = 'AND DESERT YOU!'

CRY = 'NEVER GONNA MAKE YOU CRY!'
GOODBYE = 'NEVER GONNA SAY GOODBYE'

NICE = 'Молодец. Но впредь не будь настолько алчным.'
WRONG = '*НЕПРАВИЛЬНО!*'

APPEAR = 'ПОЯВЛЯЕТСЯ РИК ЭСТЛИ ВЕРХОМ НА КАКОЙ-ТО синей тягучей.... хрени? кхм, не важно, И БЬЕТ ТЕБЯ *МИКРОФОНОМ!*\n\nК счастью тебе удалось сбежать'

def enter(user, reply):
	msg = (
		'Здесь горы из всевозможных сокровищ и тысячи, нет, миллионы золо...\n*О НЕТ, БЕГИ ЗА СВОЮ ЖИ*\n'
	)
	reply(msg)
	user.set_room_temp('question', 'first')

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	
	if question == 'first':
		return [ UP ]

	if question == 'second':
		return [ AROUND ]

	if question == 'third':
		return [ CRY, GOODBYE ]

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		if text == UP:
			reply(DOWN)
			user.set_room_temp('question', 'second')
	elif question == 'second':
		if text == AROUND:
			reply(DESERT)
			user.set_room_temp('question', 'third')
	elif question == 'third':
		if text == CRY:
			reply(NICE)
			user.leave(reply)
		elif text == GOODBYE:
			reply(WRONG)
			reply(APPEAR)
			user.hp -= 50
			if user.hp < 0:
				user.death(reply, reason='Rick Roll')
			user.leave(reply)