# burritoly
BioSecurity checking tool for warning against incompatible part combinations and pathogenic genomes 


Useful commands:

To run:
	python BurritoLy.py
Dependencies:
	For the GUI import (Using homebrew on mac):
	brew install tk 
	brew install blast
	
	To create your own database of pathogenice sequences:
	pip3 install ete3
	pip3 install xlsxwriter
	
Updating demos/Fake libraries:
	Run FakeDataBase.py to make new databases. 
	Put the swissprot.fsa and the updated newDB_gi.xlsx into the Demo Libraries folder
	Run Demos.py to create fake demos for use in the BurritoLy application
To make a db from fasta files:
	makeblastdb -in bad_db.fsa -parse_seqids -blastd_version 5 -dbtype prot
Databases missing:
	In db make a folder called swissprot and place update_blastdb.pl and run:
	update_db.pl --decompress swissprot
	blastdbcmd -entry all -db swissprot -out swiss.fsa

