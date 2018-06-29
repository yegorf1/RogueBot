import usermanager

name = 'Торговец'

def enter(user, reply):
	usr = usermanager.random_user()
	msg = (
		'Перед тобой находится какая-то будка, неумело сколоченная из каких-то кривых досок. '
		'За широкой деревянной доской (прилавок) на воображаемой табуретке сидит зеленый бугай '
		'метра 2 ростом. Серьезно, он сидит в воздухе! Завидев тебя, он что-то нечленораздельно '
		'говорит, ты понимаешь лишь:\n'
		'«Привит, юдишка! Йа есть Боба! Босс сказал Бобе таргавать!! Боба типерь умеет в тарговлю!»\n\n'
		'Зуб (Цена 1 зуб)\n'
		'Тока што выбил с {0}, дажи кечтуп ищо капаит!\n\n'
		'Палка (Цена 5 зубов)\n'
		'Плахая палка, адной такой стукнул юдишку — а она сламалась\n\n'
		'Парашок (Цена 5 зубов)\n'
		'Вкусный парашок, клянусь Горком и Морком!'
	)
	reply(msg.format(usr.name))

def get_actions(user):
	return [ 'Зуб', 'Палка', 'Парашок', 'Уйти' ]

def action(user, reply, text):
	teeths = user.get_item_by_name('tooth')
	if teeths is None:
		user_teeth_cnt = 0
	else:
		user_teeth_cnt = teeths.count
	if text == 'Зуб':
		teeth_cnt = user.get_room_temp('teeth_cnt', def_val=0)

		if user_teeth_cnt >= 1:
			if teeth_cnt > 2:
				reply('Ты давно понимаешь, что что-то идет не так, но орк выглядит вполне счастливым, и ты слышишь, как он бормочет что-то вроде: «какая харошая тарговля, босс будит даволен»')
			else:
				user.set_room_temp('teeth_cnt', teeth_cnt + 1)

			reply('Ты купил зуб! (И потратил на это зуб)')
		else:
			reply('«Нет зубов — нет товара» — хотел сказать орк, но просто ударил тебя по лицу.')
			user.make_damage(1, 10, reply, death=False)
	elif text == 'Палка':
		if user_teeth_cnt >= 5:
			reply('Забирай')
			user.add_item('good', 'mage_stick')

			user.remove_item('tooth', count=5)
		else:
			reply('«Нет зубов — нет товара» — хотел сказать орк, но просто ударил тебя по лицу.')
			user.make_damage(1, 10, reply, death=False)
	elif text == 'Парашок':
		if user_teeth_cnt >= 5:
			reply('Забирай')
			user.add_item('neutral', 'protein')

			user.remove_item('tooth', count=5)
		else:
			reply('«Нет зубов — нет товара» — хотел сказать орк, но просто ударил тебя по лицу.')
			user.make_damage(1, 10, reply, death=False)
	else:
		user.leave(reply)
