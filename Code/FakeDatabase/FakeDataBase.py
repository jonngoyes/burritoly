
   
import xlsxwriter
from random import seed
from random import randint
from datetime import date
from ete3 import NCBITaxa

if __name__ == "__main__":
    
    ''' 
    First fake database is the fake database that contains the bad sequences
    The important part is to make fake amino acid sequences of a realistic length
    It must also include the TaxID and the corresponding organsim, this is based on the NCBI database
    '''

    sheet = xlsxwriter.Workbook('newDB_gi.xlsx')
    database = sheet.add_worksheet('BurritoLy')
    bold = sheet.add_format({'bold': True})
    bold.set_bg_color('gray')
    gi = randint(1000000,100000000)

    # no J, O, U, X
    aminoAcids = ['A','R','N','D','B','C','E','Q','Z','G','H','I','L','K','M','F','P','S','T','W','Y','V']
    dbEntries = 5000
    ncbi = NCBITaxa()
    fid = open('bad_db.fsa','w')
    seq_id = 1
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

        # Now writing the above info the the Excel spreadsheet
        # First column is the GI
        gi = gi+1
        database.write(i+1,0,gi)

        # Second column is the TaxID
        database.write(i+1,1,taxID)

        # Third column is the organsim
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
        
        header = '>seq' + str(seq_id) + ' ' + str(organism[taxID])+ ' '+ str(taxID)
        fid.write(header)
        fid.write('\n')
        fid.write(sequence)
        fid.write('\n') 
        seq_id = seq_id + 1

    # Adding titles to each of the columns 

    database.write(0,0,'GI', bold)
    database.write(0,1,'TaxID', bold)
    database.write(0,2,'Organsim', bold)
    database.write(0,3,'Description', bold)
    database.write(0,4,'Pathogenic Mode', bold)
    database.write(0,5,'Agency', bold)
    database.write(0,6,'Document', bold)
    database.write(0,7,'Provision', bold)
    database.write(0,8,'Pathogen Name', bold)
    database.write(0,9,'IGSC Status', bold)
    database.write(0,10,'IGSC Risk Level', bold)
    database.write(0,11,'Sequence', bold)
    database.write(0,12,'Date of Change', bold)
    database.write(0,13,'Changed by', bold)

    sheet.close()
    fid.close()
    '''
    The second database is the pathogenic TaxID database
    This is a list of NCBI TaxIDs that can be considered pathogenic 
    The parents/children of these TaxIDs must be compared to the sequences found in Swissprot
    If there is a match that means that sequence is pathogenic 
    '''

    sheet = xlsxwriter.Workbook('newDB_TaxID.xlsx')
    database = sheet.add_worksheet('BurritoLy')
    bold = sheet.add_format({'bold': True})
    bold.set_bg_color('gray')

    dbEntries = 500

    for i in range(dbEntries):
        # Picking the random organism to be pathogenic in this fake database
        organism = 'null'
        while organism == 'null':
            taxID = randint(10000,1000000)
            organism = ncbi.get_taxid_translator([taxID])
            if organism == {}:
                organism = 'null'
        
        # Writing to the Excel spreadsheet
        # First two columns are the TaxID and the corresponding organism
        database.write(i+1, 0, taxID)
        database.write(i+1, 1, organism[taxID])

        # The next columns are text that do not matter for our algorithm
        for j in range (2,9,1):
            database.write(i+1,j, 'N/A')
        
        # Column J is the date
        database.write(i+1,9,entry)

        # Column K is the signature
        database.write(i+1,10,'BurritoLy')

    
    database.write(0,0,'TaxID', bold)
    database.write(0,1,'Organsim', bold)
    database.write(0,2,'Group', bold)
    database.write(0,3,'Agency', bold)
    database.write(0,4,'Document', bold)
    database.write(0,5,'Provision', bold)
    database.write(0,6,'Pathogen Name', bold)
    database.write(0,7,'IGSC Status', bold)
    database.write(0,8,'IGSC Risk Leve', bold)
    database.write(0,9,'Date of Change', bold)
    database.write(0,10,'Changed by', bold)
    
    sheet.close()