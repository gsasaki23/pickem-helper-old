import csv
from copy import copy

# TAKES og_db, PULLS TEAM NAMES AND RESULTS
database = []
with open('/Users/GakuSasaki/Documents/python workspace/helpPickEm/og_db.csv', 'r') as file:
    reader = csv.reader(file)
    rowNr = 0
    for row in reader:
        if rowNr >= 1:
            database.append(row)  
        rowNr = rowNr + 1
file.close()
# at this point, database is a list of lists ['seed', 'CN1', ...,'VCS1'] with each being str'wins-loss'
#   database[0] would give the list of [seed,results] and database[0][1] would give specific win-loss




'''
Condenses two score strings together.
ex) "1-1" and "2-1" returns "3-2"
'''
def condense(sc1,sc2):
    temp1 = copy(sc1).split("-")
    temp2 = copy(sc2).split("-")
    temp1[0] = int(temp1[0]) + int(temp2[0])
    temp1[1] = int(temp1[1]) + int(temp2[1])
    ans = str(temp1[0]) + "-" + str(temp1[1])
    return ans

# Sample - CN1 2-0 CN2
'''
Adds score to the database.
addData(seed,score,opponent) would add score to corresponding opponent for seed in database
ex) addData("CN1","2-0","CN2") would add "2-0" to CN1's CN2 record.

'''
def addData(seed,score,opponent):
    if seed == opponent:
        print("Error: seed should not be playing themselves")
    else:
        for data in database:
            if data[0] == seed:
                if opponent == "CN1":
                    data[1] = condense(data[1],score)
                elif opponent == "CN2":
                    data[2] = condense(data[2],score)
                elif opponent == "CN3":
                    data[3] = condense(data[3],score)
                elif opponent == "EU1":
                    data[4] = condense(data[4],score)
                elif opponent == "EU2":
                    data[5] = condense(data[5],score)
                elif opponent == "EU3":
                    data[6] = condense(data[6],score)
                elif opponent == "KR1":
                    data[7] = condense(data[7],score)
                elif opponent == "KR2":
                    data[8] = condense(data[8],score)
                elif opponent == "KR3":
                    data[9] = condense(data[9],score)
                elif opponent == "LMS1":
                    data[10] = condense(data[10],score)
                elif opponent == "LMS2":
                    data[11] = condense(data[11],score)
                elif opponent == "LMS3":
                    data[12] = condense(data[12],score)
                elif opponent == "NA1":
                    data[13] = condense(data[13],score)
                elif opponent == "NA2":
                    data[14] = condense(data[14],score)
                elif opponent == "NA3":
                    data[15] = condense(data[15],score)
                elif opponent == "SEA1":
                    data[16] = condense(data[16],score)
                elif opponent == "TR1":
                    data[17] = condense(data[17],score)
                elif opponent == "VCS1":
                    data[18] = condense(data[18],score)
                elif opponent == "BR1":
                    data[19] = condense(data[19],score)
                elif opponent == "CIS1":
                    data[20] = condense(data[20],score)
                else:
                    print("Error: opponent was not found")


def add2017():
    # 2017 Group A - KR2,NA3,LMS2,CN1
    addData("KR2","2-0","NA3")
    addData("KR2","1-1","LMS2")
    addData("KR2","2-0","CN1")
    addData("NA3","0-2","KR2")
    addData("NA3","2-0","LMS2")
    addData("NA3","1-1","CN1")
    addData("LMS2","1-1","KR2")
    addData("LMS2","0-2","NA3")
    addData("LMS2","1-1","CN1")
    addData("CN1","0-2","KR2")
    addData("CN1","1-1","NA3")
    addData("CN1","1-1","LMS2")

    # 2017 Group B - KR1,EU3,SEA1,NA2
    addData("KR1","2-0","EU3")
    addData("KR1","2-0","SEA1")
    addData("KR1","2-0","NA2")
    addData("EU3","0-2","KR1")
    addData("EU3","2-1","SEA1")
    addData("EU3","2-1","NA2")
    addData("SEA1","0-2","KR1")
    addData("SEA1","1-2","EU3")
    addData("SEA1","1-1","NA2")
    addData("NA2","0-2","KR1")
    addData("NA2","1-2","EU3")
    addData("NA2","1-1","SEA1")

    # 2017 Group C - CN2,KR3,EU1,TR1
    addData("CN2","2-0","KR3")
    addData("CN2","1-1","EU1")
    addData("CN2","2-0","TR1")
    addData("KR3","0-2","CN2")
    addData("KR3","2-0","EU1")
    addData("KR3","2-0","TR1")
    addData("EU1","1-1","CN2")
    addData("EU1","0-2","KR3")
    addData("EU1","2-0","TR1")
    addData("TR1","0-2","CN2")
    addData("TR1","0-2","KR3")
    addData("TR1","0-2","EU1")

    # 2017 Group D - CN3,EU2,NA1,LMS1
    addData("CN3","2-0","EU2")
    addData("CN3","1-1","NA1")
    addData("CN3","2-0","LMS1")
    addData("EU2","0-2","CN3")
    addData("EU2","2-1","NA1")
    addData("EU2","2-0","LMS1")
    addData("NA1","1-1","CN3")
    addData("NA1","1-2","EU2")
    addData("NA1","1-1","LMS1")
    addData("LMS1","0-2","CN3")
    addData("LMS1","0-2","EU2")
    addData("LMS1","1-1","NA1")

    # 2017 Brackets - Quarters
    addData("KR2","3-2","EU2")
    addData("EU2","2-3","KR2")
    addData("CN2","3-1","EU3")
    addData("EU3","1-3","CN2")
    addData("CN3","3-2","NA3")
    addData("NA3","2-3","CN3")
    addData("KR1","0-3","KR3")
    addData("KR3","3-0","KR1")

    # 2017 Brackets - Semis+Finals
    addData("KR2","3-2","CN2")
    addData("CN2","2-3","KR2")
    addData("CN3","1-3","KR3")
    addData("KR3","3-1","CN3")
    addData("KR2","0-3","KR3")
    addData("KR3","3-0","KR2")

def add2016():
    # 2016 Group A - KR1,CIS1,NA2,EU1
    addData("KR1","1-1","CIS1")
    addData("KR1","1-1","NA2")
    addData("KR1","2-0","EU1")
    addData("CIS1","1-1","KR1")
    addData("CIS1","2-0","NA2")
    addData("CIS1","1-1","EU1")
    addData("NA2","1-1","KR1")
    addData("NA2","0-2","CIS1")
    addData("NA2","2-0","EU1")
    addData("EU1","0-2","KR1")
    addData("EU1","1-1","CIS1")
    addData("EU1","0-2","NA2")

    # 2016 Group B - KR2,NA3,CN3,LMS1
    addData("KR2","2-0","NA3")
    addData("KR2","2-0","CN3")
    addData("KR2","1-1","LMS1")
    addData("NA3","0-2","KR2")
    addData("NA3","2-0","CN3")
    addData("NA3","1-1","LMS1")
    addData("CN3","0-2","KR2")
    addData("CN3","0-2","NA3")
    addData("CN3","2-0","LMS1")
    addData("LMS1","1-1","KR2")
    addData("LMS1","1-1","NA3")
    addData("LMS1","0-2","CN3")

    # 2016 Group C - EU2,CN1,LMS2,BR1
    addData("EU2","1-1","CN1")
    addData("EU2","1-1","LMS2")
    addData("EU2","2-0","BR1")
    addData("CN1","1-1","EU2")
    addData("CN1","2-0","LMS2")
    addData("CN1","1-1","BR1")
    addData("LMS2","1-1","EU2")
    addData("LMS2","0-2","CN1")
    addData("LMS2","2-0","BR1")
    addData("BR1","0-2","EU2")
    addData("BR1","1-1","CN1")
    addData("BR1","0-2","LMS2")

    # 2016 Group D - KR3,CN2,NA1,EU3
    addData("KR3","2-0","CN2")
    addData("KR3","1-1","NA1")
    addData("KR3","2-0","EU3")
    addData("CN2","0-2","KR3")
    addData("CN2","2-0","NA1")
    addData("CN2","1-1","EU3")
    addData("NA1","1-1","KR3")
    addData("NA1","0-2","CN2")
    addData("NA1","2-0","EU3")
    addData("EU3","0-2","KR3")
    addData("EU3","1-1","CN2")
    addData("EU3","0-2","NA1")

    # 2016 Brackets - Quarters
    addData("KR2","3-1","CN2")
    addData("CN2","1-3","KR2")
    addData("KR1","3-1","CN1")
    addData("CN1","1-3","KR1")
    addData("EU2","3-0","CIS1")
    addData("CIS1","0-3","EU2")
    addData("KR3","3-0","NA3")
    addData("NA3","0-3","KR3")

    # 2016 Brackets - Semis+Finals
    addData("KR2","3-2","KR1")
    addData("KR1","2-3","KR2")
    addData("EU2","0-3","KR3")
    addData("KR3","3-0","EU2")
    addData("KR2","3-2","KR3")
    addData("KR3","2-3","KR2")

def add2015():
    # 2015 Group A - NA1,LMS2,KR2,BR1
    addData("NA1","1-1","LMS2")
    addData("NA1","0-2","KR2")
    addData("NA1","1-1","BR1")
    addData("LMS2","1-1","NA1")
    addData("LMS2","2-0","KR2")
    addData("LMS2","1-1","BR1")
    addData("KR2","2-0","NA1")
    addData("KR2","0-2","LMS2")
    addData("KR2","2-0","BR1")
    addData("BR1","1-1","NA1")
    addData("BR1","1-1","LMS2")
    addData("BR1","0-2","KR2")

    # 2015 Group B - LMS1,NA3,EU1,CN3
    addData("LMS1","2-1","NA3")
    addData("LMS1","1-1","EU1")
    addData("LMS1","1-1","CN3")
    addData("NA3","1-2","LMS1")
    addData("NA3","1-1","EU1")
    addData("NA3","1-1","CN3")
    addData("EU1","1-1","LMS1")
    addData("EU1","1-1","NA3")
    addData("EU1","2-0","CN3")
    addData("CN3","1-1","LMS1")
    addData("CN3","1-1","NA3")
    addData("CN3","0-2","EU1")

    # 2015 Group C - SEA1,CN2,EU2,KR1
    addData("SEA1","0-2","CN2")
    addData("SEA1","0-2","EU2")
    addData("SEA1","0-2","KR1")
    addData("CN2","2-0","SEA1")
    addData("CN2","2-0","EU2")
    addData("CN2","0-2","KR1")
    addData("EU2","2-0","SEA1")
    addData("EU2","0-2","CN2")
    addData("EU2","0-2","KR1")
    addData("KR1","2-0","SEA1")
    addData("KR1","2-0","CN2")
    addData("KR1","2-0","EU2")

    # 2015 Group D - CN1,KR3,EU3,NA2
    addData("CN1","0-2","KR3")
    addData("CN1","1-1","EU3")
    addData("CN1","1-1","NA2")
    addData("KR3","2-0","CN1")
    addData("KR3","1-1","EU3")
    addData("KR3","2-0","NA2")
    addData("EU3","1-1","CN1")
    addData("EU3","1-1","KR3")
    addData("EU3","2-0","NA2")
    addData("NA2","1-1","CN1")
    addData("NA2","0-2","KR3")
    addData("NA2","0-2","EU3")

    # 2015 Brackets - Quarters
    addData("LMS2","1-3","EU3")
    addData("EU3","3-1","LMS2")
    addData("KR1","3-0","LMS1")
    addData("LMS1","0-3","EU1")
    addData("EU1","3-0","CN2")
    addData("CN2","0-3","EU1")
    addData("KR3","1-3","KR2")
    addData("KR2","3-1","KR3")

    # 2015 Brackets - Semis+Finals
    addData("EU3","0-3","KR1")
    addData("KR1","3-0","EU3")
    addData("EU1","0-3","KR2")
    addData("KR2","3-0","EU1")
    addData("KR1","3-1","KR2")
    addData("KR2","1-3","KR1")

def add2014():
    # LMS did not exist. TPA qualified as GPL#1, AHQ qualified as Garena finalists.
    # for now, seeded AHQ as LMS1, TPA as LMS2
    
    # 2014 Group A - KR2,CN1,LMS1,TR1
    addData("KR2","2-0","CN1")
    addData("KR2","2-0","LMS1")
    addData("KR2","2-0","TR1")
    addData("CN1","0-2","KR2")
    addData("CN1","2-1","LMS1")
    addData("CN1","0-2","TR1")
    addData("LMS1","0-2","KR2")
    addData("LMS1","1-2","CN1")
    addData("LMS1","2-0","TR1")
    addData("TR1","0-2","KR2")
    addData("TR1","0-2","CN1")
    addData("TR1","0-2","LMS1")

    # 2014 Group B - CN2,NA1,EU3,LMS2
    addData("CN2","1-1","NA1")
    addData("CN2","2-0","EU3")
    addData("CN2","2-0","LMS2")
    addData("NA1","1-1","CN2")
    addData("NA1","1-1","EU3")
    addData("NA1","2-0","LMS2")
    addData("EU3","0-2","CN2")
    addData("EU3","1-1","NA1")
    addData("EU3","1-1","LMS2")
    addData("LMS2","0-2","CN2")
    addData("LMS2","0-2","NA1")
    addData("LMS2","1-1","EU3")

    # 2014 Group C - NA3,EU2,CN3,KR1
    addData("NA3","1-1","EU2")
    addData("NA3","1-1","CN3")
    addData("NA3","0-2","KR1")
    addData("EU2","1-1","NA3")
    addData("EU2","0-2","CN3")
    addData("EU2","1-1","KR1")
    addData("CN3","1-1","NA3")
    addData("CN3","2-0","EU2")
    addData("CN3","0-2","KR1")
    addData("KR1","2-0","NA3")
    addData("KR1","1-1","EU2")
    addData("KR1","2-0","CN3")

    # 2014 Group D - KR3,NA3,EU1,BR1
    addData("KR3","2-1","NA3")
    addData("KR3","1-1","EU1")
    addData("KR3","2-0","BR1")
    addData("NA3","1-2","KR3")
    addData("NA3","1-1","EU1")
    addData("NA3","2-0","BR1")
    addData("EU1","1-1","KR3")
    addData("EU1","1-1","NA3")
    addData("EU1","1-1","BR1")
    addData("BR1","0-2","KR3")
    addData("BR1","0-2","NA3")
    addData("BR1","1-1","EU1")

    # 2014 Brackets - Quarters
    addData("KR2","3-1","NA1")
    addData("NA1","1-3","KR2")
    addData("KR1","3-1","NA3")
    addData("NA3","1-3","KR1")
    addData("CN2","3-2","CN1")
    addData("CN1","2-3","CN2")
    addData("KR3","0-3","CN3")
    addData("CN3","3-0","KR3")

    # 2014 Brackets - Semis+Finals
    addData("KR2","3-0","KR1")
    addData("KR1","0-3","KR2")
    addData("CN2","3-2","CN3")
    addData("CN3","2-3","CN2")
    addData("KR2","3-1","CN2")
    addData("CN2","1-3","KR2")

def add2013():
    # LMS did not exist. Listing Gamania Bears (TW/HK/MO Champion) as LMS1
    # "seeding' did not exactly exist.
    # NA: C9, TSM, Vulcun
    # CN: Royal, OMG
    # KR: NajinBlack, Samsung, SKT (Samsung was KR Circuit 2nd, SKT was regionals 1st)
    # EU: FNC, LD, Gambit
    # CIS and SEA.

    # 2013 Group A - KR3, CN2, EU2 ,NA2, CIS1
    addData("KR3","1-1","CN2")
    addData("KR3","2-0","EU2")
    addData("KR3","2-0","NA2")
    addData("KR3","2-0","CIS1")
    addData("CN2","1-1","KR3")
    addData("CN2","2-0","EU2")
    addData("CN2","2-0","NA2")
    addData("CN2","2-0","CIS1")
    addData("EU2","0-2","KR3")
    addData("EU2","0-2","CN2")
    addData("EU2","1-1","NA2")
    addData("EU2","2-0","CIS1")
    addData("NA2","0-2","KR3")
    addData("NA2","0-2","CN2")
    addData("NA2","1-1","EU2")
    addData("NA2","1-1","CIS1")
    addData("CIS1","0-2","KR3")
    addData("CIS1","0-2","CN2")
    addData("CIS1","0-2","EU2")
    addData("CIS1","1-1","NA2")

    # 2013 Group B - EU1, EU3, KR2, NA3, SEA1
    addData("EU1","2-0","EU3")
    addData("EU1","2-0","KR2")
    addData("EU1","1-1","NA3")
    addData("EU1","2-0","SEA1")
    addData("EU3","0-2","EU1")
    addData("EU3","2-1","KR2")
    addData("EU3","2-0","NA3")
    addData("EU3","2-0","SEA1")
    addData("KR2","0-2","EU1")
    addData("KR2","1-2","EU3")
    addData("KR2","2-0","NA3")
    addData("KR2","2-0","SEA1")
    addData("NA3","1-1","EU1")
    addData("NA3","0-2","EU3")
    addData("NA3","0-2","KR2")
    addData("NA3","2-0","SEA1")
    addData("SEA1","0-2","EU1")
    addData("SEA1","0-2","EU3")
    addData("SEA1","0-2","KR2")
    addData("SEA1","0-2","NA3")

    # 2013 Brackets - Quarters. BEST OF 3 NOT 5.
    addData("LMS1","0-2","KR3")
    addData("KR3","2-0","LMS1")
    addData("KR1","2-1","EU3")
    addData("EU3","1-2","KR1")
    addData("CN1","2-0","CN2")
    addData("CN2","0-2","CN1")
    addData("NA1","1-2","EU1")
    addData("EU1","2-1","NA1")

    # 2013 Brackets - Semis+Finals
    addData("KR3","3-2","KR1")
    addData("KR1","2-3","KR3")
    addData("CN1","3-1","EU1")
    addData("EU1","1-3","CN1")
    addData("KR3","3-0","CN1")
    addData("CN1","0-3","KR3")

def add2012():
    # KR and CN only have 2 seeds.
    
    # 2012 Group A - KR1, CN2, NA3, EU2. ROUND ROBIN X1 NOT 2.
    addData("KR1","1-0","CN2")
    addData("KR1","1-0","NA3")
    addData("KR1","1-0","EU2")
    addData("CN2","0-1","KR1")
    addData("CN2","1-0","NA3")
    addData("CN2","1-0","EU2")
    addData("NA3","0-1","KR1")
    addData("NA3","0-1","CN2")
    addData("NA3","1-0","EU2")
    addData("EU2","0-1","KR1")
    addData("EU2","0-1","CN2")
    addData("EU2","0-1","NA3")

    # 2012 Group B - KR2,EU3,SEA1,NA2. ROUND ROBIN X1 NOT 2.
    addData("KR2","1-0","EU3")
    addData("KR2","1-0","SEA1")
    addData("KR2","1-0","NA2")
    addData("EU3","0-1","KR2")
    addData("EU3","1-0","SEA1")
    addData("EU3","1-0","NA2")
    addData("SEA1","0-1","KR2")
    addData("SEA1","0-1","EU3")
    addData("SEA1","1-0","NA2")
    addData("NA2","0-1","KR2")
    addData("NA2","0-1","EU3")
    addData("NA2","0-1","SEA1")

    # 2012 Brackets - Quarters. BEST OF 3 NOT 5.
    addData("EU1","2-0","CN2")
    addData("CN2","0-2","EU1")
    addData("LMS1","2-0","KR2")
    addData("KR2","0-2","LMS1")
    addData("NA1","0-2","KR1")
    addData("KR1","2-0","NA1")
    addData("CN1","1-2","EU3")
    addData("EU3","2-1","CN1")

    # 2012 Brackets - Semis+Finals. SEMIS BEST OF 3 NOT 5.
    addData("EU1","1-2","LMS1")
    addData("LMS1","2-1","EU1")
    addData("KR1","2-1","EU3")
    addData("EU3","1-2","KR1")
    addData("LMS1","3-1","KR1")
    addData("KR1","1-3","LMS1")



def add2011():
    # KR and CN did not participate.
    # SEA has two teams with no seeds, added both as SEA1.
    
    # 2011 Group A - NA2, EU1, EU3, SEA1. ROUND ROBIN X1 NOT 2.
    addData("NA2","1-0","EU1")
    addData("NA2","1-0","EU3")
    addData("NA2","1-0","SEA1")
    addData("EU1","0-1","NA2")
    addData("EU1","1-0","EU3")
    addData("EU1","1-0","SEA1")
    addData("EU3","0-1","NA2")
    addData("EU3","0-1","EU1")
    addData("EU3","1-0","SEA1")
    addData("SEA1","0-1","NA2")
    addData("SEA1","0-1","EU1")
    addData("SEA1","0-1","EU3")

    # 2011 Group B - NA1,NA3,EU2,SEA1. ROUND ROBIN X1 NOT 2.
    addData("NA1","1-0","NA3")
    addData("NA1","1-0","EU2")
    addData("NA1","0-1","SEA1")
    addData("NA3","0-1","NA1")
    addData("NA3","1-0","EU2")
    addData("NA3","1-0","SEA1")
    addData("EU2","0-1","NA1")
    addData("EU2","0-1","NA3")
    addData("EU2","1-0","SEA1")
    addData("SEA1","1-0","NA1")
    addData("SEA1","0-1","NA3")
    addData("SEA1","0-1","EU2")

    # 2011 Brackets - Quarters. BEST OF 3 NOT 5.
    addData("EU1","2-0","EU2")
    addData("EU2","0-2","EU1")
    addData("NA3","1-2","EU3")
    addData("EU3","2-1","NA3")
    
    # 2011 Brackets - Semis+Finals. BOTH BEST OF 3 NOT 5.
    addData("EU1","2-1","NA1")
    addData("NA1","1-2","EU1")
    addData("NA2","0-2","EU3")
    addData("EU3","2-0","NA2")
    addData("EU1","0-2","EU3")
    addData("EU3","2-0","EU1")

    # 2011 BRACKETS - Losers, best of 3. Some games include the extended rule - bo3 starting 1-0 based on previous meeting
    addData("EU2","0-1","NA3")
    addData("NA3","1-0","EU1")
    addData("NA1","2-0","NA2")
    addData("NA2","0-2","NA1")
    addData("EU1","2-0","NA1")
    addData("NA1","0-2","EU1")

    # 2011 Brackets - Grand Finals. includes the extended rule - bo3 starting 1-0 based on previous meeting
    addData("EU3","2-1","EU1")
    addData("EU1","1-2","EU3")

add2011()
add2012()
add2013()
add2014()
add2015()
add2016()
add2017()

# Takes databse and prints to a csv
csvheader = [['seed','CN1','CN2','CN3','EU1','EU2','EU3','KR1','KR2','KR3',
              'LMS1','LMS2','LMS3','NA1','NA2','NA3','SEA1','TR1','VCS1','BR1','CIS1']]
to_write = [copy(database)]
with open('og_db_added.csv','w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvheader)
    rowNr = 0
    for seed in to_write:
        writer.writerows(to_write[rowNr])
        rowNr += 1
csvFile.close()
