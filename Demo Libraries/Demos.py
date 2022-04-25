'''
This file is creating the test cases for BurritoLy

Want test cases that show off several features

1. Shows off the ability to detect good/bad people
2. Shows off the ability to remove bad sequences when strung together
'''

import json
import string
import random
from random import randint
from ete3 import NCBITaxa
import pandas as pd
import numpy as np

'''
The dictionary should include

part type, name, sequence

'''

def getName(part):
    letterCode = ''
    for i in range(3):
        letterCode = letterCode + random.choice(string.ascii_letters)

    numCode = ''
    for i in range(2):
        numCode =  numCode + str(randint(0,10))

    name = part + '_' + letterCode + numCode
    return name


if __name__ == "__main__":
    partTypes = ['promoter', 'RBS', 'gene', 'terminator']

    findDict = [0 for i in range(60)]
    badDictionary = {"parts": findDict}

    df = pd.read_excel('newDB_gi.xlsx',sheet_name='BurritoLy')
    badSeq = df.Sequence

    for i in range(60):
        partNum = randint(0,3)
        part = partTypes[partNum]
        name = getName(part)

        seqNum = randint(0, len(badSeq)-1)
        sequence = badSeq[seqNum]

        tempDict = {
            "part": part,
            "name": name,
            "sequence": sequence
        }

        badDictionary["parts"][i] = tempDict

    badDict = json.dumps(badDictionary, indent = 4)

    with open("badDemo.json","w") as outfile:
        outfile.write(badDict)



