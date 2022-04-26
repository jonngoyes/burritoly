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
    lineage = getLineage(taxID)
    df = pd.read_excel('newDB_TaxID.xlsx',sheet_name='BurritoLy') #consider opening beforehand

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

    print('\n\n')
    return badTax, good

    


