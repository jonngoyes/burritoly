
	# search_db(query_in = 'realfasta')
	# read_output()
from state_class import *
from functions import *

# device = toolDeviceThing()

# device.on_event('start search')
# device.on_event('search finished')


burritoly = toolDeviceThing()
burritoly.on_event('search database')
RUNNING = True
while RUNNING:
	if burritoly.state.name == 'searchState':
		search_db(query_in = 'realfasta')
		read_output()
		print('second')
	elif burritoly.state.name == 'editState':
		pass
	else : # idleState
		pass




	RUNNING = False


