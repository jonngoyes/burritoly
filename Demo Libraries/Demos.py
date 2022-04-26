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
from Bio import SeqIO

'''
The dictionary should include

part type, name, sequence

'''

def getName(part):
    '''
    This function just randomly generates a name for a part
    The format of the name is just partname_XYZ12
    Part type followed by three letters and two numbers
    '''

    letterCode = ''
    for i in range(3):
        letterCode = letterCode + random.choice(string.ascii_letters)

    numCode = ''
    for i in range(2):
        numCode =  numCode + str(randint(0,10))

    name = part + '_' + letterCode + numCode
    return name


def splitSequence(sequence):
    '''
    This function randomly separates the sequence at a random point in the string
    This will be used to create sequences that become bad when put together
    '''

    splitAt = randint(0,len(sequence)-1)
    sequence = str(sequence)
    beg = sequence[0:splitAt]
    end = sequence[(splitAt+1):(len(sequence)-1)]

    return beg, end

def makeRandomSequence():
    '''
    This function just creates a random sequence of amino acids
    The sequence is between 50 and 300 amino acids long
    '''

    aminoAcids = ['A','R','N','D','B','C','E','Q','Z','G','H','I','L','K','M','F','P','S','T','W','Y','V']
    sequenceLen = randint(50,300)
    sequence = ''

    for j in range(sequenceLen):
        acid = randint(0,21)
        sequence = sequence + aminoAcids[acid]

    return sequence


def createBadPartsWhenTogether():

    '''
    This will randomly generate 2 parts that are bad when put in a sequence together
    The goal is to show that the program recognizes that these two parts put together is bad
    The program should remove the following part from the parts list option because it would be hazard when together
    '''

    # Making the random sequences to append
    firstSeq = makeRandomSequence()
    secondSeq = makeRandomSequence()

    # Reading in a random bad sequence
    df = pd.read_excel('newDB_gi.xlsx',sheet_name='BurritoLy')
    badSeq = df.Sequence

    seqNum = randint(0, len(badSeq)-1)
    sequence = badSeq[seqNum]

    # Taking the bad sequence and splitting it and appending to the random sequence
    [beg, end] = splitSequence(sequence)
    sequence1 = firstSeq + beg
    sequence2 = end + secondSeq

    partTypes = ['promoter', 'RBS', 'gene', 'terminator']
    partNum = randint(0,2)
    # Want the part types to follow each other so it makes sense to remove it
    part1 = partTypes[partNum]
    part2 = partTypes[partNum+1]

    badPart1 = {
        "part": part1,
        "name": getName(part1),
        "sequence": sequence1
    }

    badPart2 = {
        "part": part2,
        "name": getName(part2),
        "sequence": sequence2
    }

    return badPart1, badPart2 

def createBadPart():
    '''
    This just takes a part from the bad GI database and formats it appropriately
    These parts should always be flagged immediately as bad by the program
    '''

    df = pd.read_excel('newDB_gi.xlsx',sheet_name='BurritoLy')
    badSeq = df.Sequence

    partTypes = ['promoter', 'RBS', 'gene', 'terminator']
    partNum = randint(0,3)
    part = partTypes[partNum]
    name = getName(part)

    seqNum = randint(0, len(badSeq)-1)
    sequence = badSeq[seqNum]

    badPart = {
        "part": part,
        "name": name,
        "sequence": sequence
    }

    return badPart

def createGoodPart():
    '''
    This takes a sequence from the swissprot database 
    It then converts it into a good part
    These parts should never be flagged by the algorithm
    ^^ unless it accidentally matches our randomly generated database; probability low though
    '''

    partTypes = ['promoter', 'RBS', 'gene', 'terminator']
    partNum = randint(0,3)
    part = partTypes[partNum]
    name = getName(part)

    fasta_sequences = SeqIO.parse(open('swissprot.fsa'),'fasta')

    # Hard coding the length to be 47886 because its broken
    #time = randint(0, sum(1 for _ in fasta_sequences))
    # The hard coding is based on the above line for what the max time would be 

    seqNum = randint(0,47885)

    count = 0
    for sequ in fasta_sequences:
        if seqNum == count:
            sequence = str(sequ.seq)
        count = count + 1

    goodPart = {
        "part": part,
        "name": name,
        "sequence": sequence
    }

    return goodPart

def createRandomPartLibrary(libLen, badEnabled):
    '''
    This library creates a realistic parts library of someone who's library can contain both good and bad parts
    There is a mix in their library and it is relatively random with what types of parts are in there 

    libLen is the length of the library
    badEnabled is a Boolean and explains whether or not they want purely bad parts or not
    '''

    temp = [0 for i in range(libLen)]
    dictionary = {"parts": temp}
    slotsLeft = libLen
    count = 0

    while slotsLeft != 0:
        # Picking which of the type the parts is
        if slotsLeft != 1:
            # As long as there is at least two slots, bad parts when together is an option
            addition = randint(1,3)
        else:
            addition = randint(1,2)

        '''
        Giving the option to not have bad parts
        People realistically can not know that their parts are bad when put together
        So when badEnabled = True, truly bad parts can be added
        when badEnabled = False, only good parts are added, with the chance that it's bad when put together 
        '''

        # Adding parts to the dictionary 
        if addition == 2 and badEnabled == True:
            part = createBadPart()
            slotsLeft = slotsLeft - 1
            dictionary["parts"][count] = part
        if addition == 2 and badEnabled == False:
            # If bad is not enabled, we will have to pick between the other two options of parts
            addition = randint(1,2)
            if addition == 2 and slotsLeft != 1:
                addition = 3
            else:
                addition = 1
        if addition == 1:
            part = createGoodPart()
            slotsLeft = slotsLeft - 1
            dictionary["parts"][count] = part
        if addition == 3:
            part1, part2 = createBadPartsWhenTogether()
            slotsLeft = slotsLeft - 2
            dictionary["parts"][count] = part1
            count = count + 1
            dictionary["parts"][count] = part2
        
        count = count + 1
    
    return dictionary


if __name__ == "__main__":
    
    newDict = createRandomPartLibrary(50, True)
    partLib = json.dumps(newDict, indent = 4)

    with open("badPerson.json","w") as outfile:
        outfile.write(partLib)

    print("first file written \n")

    newDict = createRandomPartLibrary(50, False)
    partLib = json.dumps(newDict, indent = 4)

    
    with open("okayPersonDemo.json","w") as outfile:
        outfile.write(partLib)

    print("second file written \n")
   



