
import subprocess
from FakeDatabase.Lineage import *
def search_good_db(db_in = 'swissprot', query_in = 'fakefastaJawn', results_out = 'results.out'):


	db = "db/" + db_in +"/" + db_in 
	query = "queries/" + query_in + ".fsa"
	results = results_out

	search_database = subprocess.run(["blastp", "-db", db ,"-query", query, "-out", results, "-outfmt", "6 sseqid bitscore evalue staxids"])
	return 0

def search_bad_db(query_in = 'fakefastaJawn', results_out = 'results.out'):
	bad_db = "FakeDatabase/bad_db.fsa"
	query = "queries/" + query_in + ".fsa"
	results = results_out
	search_database = subprocess.run(["blastp", "-db", bad_db ,"-query", query, "-out", results, "-outfmt", "6 sseqid bitscore evalue"])
	return 0
