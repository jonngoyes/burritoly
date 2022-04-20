import xlsxwriter
from random import seed
from random import randint
from datetime import date
from ete3 import NCBITaxa

if __name__ == "__main__":
    # no J, O, U, X
    aminoAcids = ['A','R','N','D','B','C','E','Q','Z','G','H','I','L','K','M','F','P','S','T','W','Y','V']
    dbEntries = 2000
    ncbi = NCBITaxa()

    sheet = xlsxwriter.Workbook('newDB_gi.xlsx')
    database = sheet.add_worksheet('BurritoLy')

    for i in range(dbEntries):
    
        # Picking the length of the sequence
        sequenceLen = randint(100,500)

        # Randomizing the amino acids in a given sequence 
        sequence = ''
        for j in range(sequenceLen):
            acid = randint(0,21)
            sequence = sequence + aminoAcids[acid]

        organism = 'null'
        while organism == 'null':
            taxID = randint(10000,1000000)
            organism = ncbi.get_taxid_translator([taxID])
            if organism == {}:
                organism = 'null'
            #print(organism) 

        # Now writing the above info the the Excel spreadsheet
        # First column is the GI
        gi = randint(1000000,100000000)
        database.write(i+1,0,gi)

        # Second column is the TaxID
        #taxID = randint(1,1000)
        database.write(i+1,1,taxID)

        # Third column is the organsim
        #organism = 'fish'
        database.write(i+1,2,organism[taxID])

        # Columns D-K are just text that do not matter for our algorithm
        for j in range(3,11,1):
            database.write(i+1,j,'N/A')

        # Column L is the sequence 
        database.write(i+1,11,sequence)

        # Column M is the date
        today = date.today()
        entry = today.strftime("%m/%d/%Y")
        database.write(i+1,12,entry)

        # Column N is the initials 
        database.write(i+1,13,'BurritoLy')

    sheet.close()





