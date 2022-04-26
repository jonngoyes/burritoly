

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

class userPerson(object):
	def __init__(self,user_id = None, depth = 10, min_score = 800):
		self.user_id = user_id
		self.devices = []
		self.search_score = []
		self.depth = depth
		self.min_score = min_score
	def addDevice (self, toolDeviceThing):
		self.device.append(toolDeviceThing)
	def removeDevice(self, toolDeviceThing):
		self.device.pop()
	def printRating(self):
		return self.search_score
	def readOutput(self, results = 'results.out'):
		fid_user = open('UserHistory' + self.user_id +'.txt','a')
		fid = open(results,'r')
		arr = fid.readline()
		arr_list = arr.split()
		score = int(arr_list[1])
		avg_score = score
		count = 1
		#print(arr.type())
		while (score > self.min_score):
			print(arr)
			arr_list = arr.split()
			score = int(arr_list[1])
			fid_user.write(arr)
			if (score < self.min_score):
				print("Number of hits: ",count)
				break
			avg_score = score + avg_score
			arr = fid.readline()

			count = count + 1
		print ("Results saved in: ",results)
		print()
		avg_score = avg_score/count

		if (len(self.search_score) > self.depth):
			self.search_score.pop(0)
		self.search_score.append(avg_score)

		fid_user.close()
		fid.close()
		return 0
	def nosy(self):
		fid = open('UserHistory'+self.user_id+'txt')







