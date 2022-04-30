# burritoly
BioSecurity checking tool for warning against incompatible part combinations and pathogenic genomes 


Useful commands:


                   

Make a list of fasta sequences from the NCBI database files
		blastdbcmd -entry all -db swissprot -out swissprot.fsa

Make a blast database from a list of fasta sequences
		makeblastdb -in swissprot.fsa -dbtype nucl -parse_seqids  

Run a normal query vs the swissprot database
		DONT USE THIS:
		blastn -db db/swissprot/swissprot.fsa -query queries/fakefastaJawn.fsa -out results.out
		THIS IS BETTER:
		blastp -db db/swissprot/swissprot -query queries/realfasta.fsa -out results.out

To make a db from fasta files:
		makeblastdb -in bad_db.fsa -parse_seqids -blastd_version 5 -dbtype prot