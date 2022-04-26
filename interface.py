
	# search_db(query_in = 'realfasta')
	# read_output()
from state_class import *
from functions import *

# device = toolDeviceThing()

# device.on_event('start search')
# device.on_event('search finished')


burritoly = toolDeviceThing()
Jon = userPerson(user_id = '191')
burritoly.on_event('search database')
RUNNING = True
while RUNNING:
	if burritoly.state.name == 'searchState':
		search_db(query_in = 'realfasta')
		Jon.readOutput()
		search_db(query_in = 'fakefastaJawn')
		Jon.readOutput()

		#print(Jon.printRating())
		#read_output()
	elif burritoly.state.name == 'editState':
		pass
	else : # idleState
		pass




	RUNNING = False


