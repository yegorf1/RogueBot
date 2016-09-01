name = 'Сундук'

actions = [ 'Открыть сундку', 'Уйти' ]

hp = 50
damage_range = ( 50, 50 )

coins = 500

loot = [ ]

def get_actions(user):
	return actions

def enter(user, reply):
	reply('Ты заходишь в комнату и видешь сундук.\nОбычный сундук')


def action(user, reply, text):

	if text == actions[0]:
		reply(
			'Ты подходишь к сундуку...\n'
			'...\n'
			'...\n'
			'...\n'
			'...\n'
			'...\n'
			'_МИМИК_\n'
		)