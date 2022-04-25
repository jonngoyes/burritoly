from Lineage import *

if __name__ == "__main__":
    badtaxID = 832172 
    badLineage = 1437201
    goodtaxID = 29372

    #print('test')

    
    #check1, bad = checkLineage(badtaxID)
    check2, badParent = checkLineage(badLineage)
    #check3, good = checkLineage(goodtaxID)

    
    print(str(badtaxID) + ' returned a match of ' + str(check1))
    print(str(badLineage) + ' returned a match of ' + str(check2))
    print(str(goodtaxID) + ' returned a match of ' + str(check3))
    