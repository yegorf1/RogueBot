from constants import *

name = 'Архимаг из прошлых эпох'

hp = 50
element = NONE
damage_range =  ( 15, 20 )

coins = 3

loot = [ 'mage_amulet' ]

def enter(user, reply):
	reply('Перед вами чудовищное существо, имеющее человеческое тело, покрытое пятнами красного и черного цвета, и хвост, «украшенный» костяным набалдашником. ')
