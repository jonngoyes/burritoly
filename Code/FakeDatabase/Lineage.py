'''
This is for the main function that checks the parents of the TaxID
'''
from ete3 import NCBITaxa
import pandas as pd
import numpy as np

def getLineage(taxID):
    lineage = []

    # Getting the NCBI TaxID information
    ncbi = NCBITaxa()

    # Function automattically returns 
    lineage = ncbi.get_lineage(taxID)

    return lineage

# Idk whether or not to take in the database as an input or load it in
def checkLineage(taxID):
    '''
    Returns good = 0 if the sequence is good
    Returns good = 1 if the sequence is bad
    '''

    lineage = getLineage(taxID)
    df = pd.read_excel('FakeDatabase/newDB_TaxID.xlsx',sheet_name='BurritoLy')

    database = df.TaxID

    good = 0
    badTax = 'none' # Assuming it is not pathogenic

    for organism in lineage:
        for pathogen in database:
            if organism == pathogen: 
                badTax = organism
                good = 1

            if taxID == pathogen:
                badTax = taxID
                good = 1

    return badTax, good

    


