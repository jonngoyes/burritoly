import random 
import string

gene_name = input('Enter the gene name: ')

base_length = input('Enter the base pair length: ')
base_length = int(base_length)
header = ("> GENE {} \n".format(gene_name))
sequence = ""
base_pairs =["A", "T", "C", "G"]
for base in range(base_length):
	sequence = sequence + str(random.choice(base_pairs))

fid = open("fakefasta{}.fsa".format(gene_name),"w")
fid.write(header)
fid.write(sequence)
fid.close()


