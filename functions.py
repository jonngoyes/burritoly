
import subprocess	
def search_db(db_in = 'swissprot', query_in = 'fakefastaJawn', results_out = 'results.out'):

	# if (db_in == 'swissprot'):
	# 	db = "db/swissprot/swissprot.fsa"
	# else:
	# 	Print("Error in db")
	# if (query_in == 'fakefastaJawn'):
	# 	query = 'queries/fakefastaJawn.fsa'
	# else:
	# 	Print("Error in query")
	# if (results_out	== 'results.out'):
	# 	results = 'results.out'
	# else:
	# 	Print("Error in results")

	db = "db/" + db_in +"/" + db_in 
	query = "queries/" + query_in + ".fsa"
	results = results_out

	search_database = subprocess.run(["blastp", "-db", db ,"-query", query, "-out", results, "-outfmt", "6 delim= "])
	return 0
def read_output(results = 'results.out', min_score = 800):
	fid = open(results,'r')
	arr = fid.readline()
	arr_list = arr.split()
	score = int(arr_list[11])
	count = 1
	#print(arr.type())
	while (score > min_score):
		print(arr)
		arr = fid.readline()
		arr_list = arr.split()
		score = int(arr_list[11])
		if (score < min_score):
			print("Number of hits: ",count)
			break
		count = count + 1
	return 0
