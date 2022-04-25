

class STATE(object):

	def __init__(self):
		print ('Processing current state: ', str(self))
		self.name = str(self)
	def on_event(self,event):
		pass
	def __repr__(self):
		return self.__str__()
	def __str__(self):
		return self.__class__.__name__

class searchState(STATE):
	def __init__(self):
		self.name = 'searchState'
	def on_event(self, event):
		if event == 'search finished':
			return idleState()
		return self
class idleState(STATE):
	def __init__(self):
		self.name = 'idleState'
	def on_event(self,event):
		if event == 'search database':
			return searchState()
		if event == 'edit parts':
			return editState()
		return self
class editState(STATE):
	def __init__(self):
		self.name = 'editState'
	def on_event(self,event):
		if event == 'done editing':
			return idleState()
		return self

class toolDeviceThing(STATE):

	def __init__(self):
		self.state = idleState()

	def on_event(self,event):

		self.state = self.state.on_event(event)


