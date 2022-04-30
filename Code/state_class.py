from FakeDatabase.Lineage import *
import subprocess
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
	def __init__(self,user_id = None, depth = 10, evalue = 1.00*10**(-70), min_score = 500):
		self.user_id = user_id
		self.devices = []
		self.search_score = []
		self.depth = depth
		self.min_score = min_score
		self.evalue = evalue
		self.flag_history = []
		self.banned_status = False
		self.bad_found = False

	def addDevice (self, toolDeviceThing):
		self.device.append(toolDeviceThing)
	def removeDevice(self, toolDeviceThing):
		self.device.pop()
	def printRating(self):
		return self.search_score
	def raiseFlag(self):
		if (len(self.flag_history )> 5):
			self.flag_history.pop(0)
		self.flag_history.append(1)
		if (sum(self.flag_history )== 5):
			print("you are bad")
			self.banned_status = True
			return 1 #a bad user
		else:
			return 0
	def search_good_db(self,db_in = 'swissprot', query_in = 'fakefastaJawn', results_out = 'results.out'):
		db = "db/" + db_in +"/" + db_in 
		query = "queries/" + query_in + ".fsa"
		results = results_out
		search_database = subprocess.run(["blastp", "-db", db ,"-query", query, "-out", results, "-outfmt", "6 sseqid bitscore evalue staxids"])
		return 0

	def search_bad_db(self,query_in = 'fakefastaJawn', results_out = 'results.out'):
		bad_db = "FakeDatabase/bad_db.fsa"
		query = "queries/" + query_in + ".fsa"
		results = results_out
		search_database = subprocess.run(["blastp", "-db", bad_db ,"-query", query, "-out", results, "-outfmt", "6 sseqid bitscore evalue"])
		return 0
	def readBadOutput(self, results = 'results.out'):
		fid_user = open('UserHistory' + self.user_id +'.txt','a')
		fid = open(results,'r')
		arr = fid.readline()
		arr_list = arr.split()
		evalue = float(arr_list[2])
		count = 1
		self.bad_found = False
		#print(arr.type())
		if (evalue < self.evalue):
			bad = self.raiseFlag()
			self.bad_found = True
			if (bad == 1):
				return 1
		while (evalue < self.evalue):
			print(arr)
			arr_list = arr.split()
			evalue = float(arr_list[2])
			fid_user.write(arr)
			if (evalue >self.evalue):
				print("Number of hits: ",count)
				break
			arr = fid.readline()
			count = count + 1
		print ("Results saved in: ",results)


		fid_user.close()
		fid.close()
		return 0
	def readGoodOutput(self, results = 'results.out'):
		fid_user = open('UserHistory' + self.user_id +'.txt','a')
		fid = open(results,'r')
		arr = fid.readline()
		arr_list = arr.split()
		evalue = float(arr_list[2])
		tax_id = (arr_list[3]).split(';')
		for idx in tax_id:
			print(checkLineage(idx)[1])
			if (checkLineage(idx)[1] == 1 ):
				bad = self.raiseFlag()
				if( bad ==1):
					return 1
			

		count = 1
		if (evalue < self.evalue):
			bad = self.raiseFlag()
			if (bad == 1):
				return 1
		while (evalue < self.evalue):
			print(arr)
			arr_list = arr.split()
			evalue = float(arr_list[2])
			fid_user.write(arr)
			if (evalue > self.evalue):
				print("Number of hits: ",count)
				break
			arr = fid.readline()
			tax_id = (arr_list[3]).split(';')
			for idx in tax_id:
				print(checkLineage(idx)[1])
				if (checkLineage(idx)[1] == 1 ):
					bad = self.raiseFlag()
					if( bad ==1):
						return 1
			count = count + 1
		print ("Results saved in: ",results)


		fid_user.close()
		fid.close()
		return 0
		#print(arr.type())
		# while (score > self.min_score):
		# 	print(arr)
		# 	arr_list = arr.split()
		# 	score = float(arr_list[1])
		# 	fid_user.write(arr)
		# 	if (score < self.min_score):
		# 		print("Number of hits: ",count)
		# 		break
		# 	avg_score = score + avg_score
		# 	arr = fid.readline()

		# 	count = count + 1
		# print ("Results saved in: ",results)
		# avg_score = avg_score/count

		# if (len(self.search_score) > self.depth):
		# 	self.search_score.pop(0)
		# self.search_score.append(avg_score)

		# fid_user.close()
		# fid.close()
		# return 0
	def nosy(self):
		fid = open('UserHistory'+self.user_id+'txt')







