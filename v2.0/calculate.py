import csv
from copy import copy
import random
import secrets

# TAKES og_db, PULLS TEAM NAMES AND RESULTS
database = []
with open('/Users/GakuSasaki/Documents/python workspace/helpPickEm/og_db_added.csv', 'r') as file:
    reader = csv.reader(file)
    rowNr = 0
    for row in reader:
        if rowNr >= 1:
            database.append(row)  
        rowNr = rowNr + 1
file.close()
# at this point, database is a list of lists ['seed', 'CN1', ...,'VCS1'] with each being str'wins-loss'
#   database[0] would give the list of [seed,results] and database[0][1] would give specific win-loss

#print("Database of game wins/losses from 2011-2017 world championships: \n" + str(database))

'''
Given seed name, returns index for the seed
'''
def find_index(seed):
    temp = str(copy(seed))
    switcher = {
        "CN1":0, "CN2":1, "CN3":2, 
        "EU1":3, "EU2":4, "EU3":5,
        "KR1":6, "KR2":7, "KR3":8,
        "LMS1":9, "LMS2":10, "LMS3":11,
        "NA1":12, "NA2":13, "NA3":14,
        "SEA1":15,"TR1":16, "VCS1":17,
        "BR1":18, "CIS1":19
    }
    return switcher.get(temp,0)
'''
Given seed name, returns index for the seed IF THEY ARE THE OPPONENT
'''
def find_index_opponent(seed):
    temp = str(copy(seed))
    switcher = {
        "CN1":1, "CN2":2, "CN3":3, 
        "EU1":4, "EU2":5, "EU3":6,
        "KR1":7, "KR2":8, "KR3":9,
        "LMS1":10, "LMS2":11, "LMS3":12,
        "NA1":13, "NA2":14, "NA3":15,
        "SEA1":16,"TR1":17, "VCS1":18,
        "BR1":19, "CIS1":20
    }
    return switcher.get(temp,0)
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
'''
Returns win pct given score string as string
ex) "1-3" returns "25.00% win chance from 1 of 4 games"
'''
def calculate_win_pct(record):
    temp = copy(record).split("-")
    tot_games = 0
    for i in temp:
        tot_games += int(i)
    wins = int(temp[0])
    # if no prev matchup
    if tot_games == 0:
        return 0.5
    return wins/tot_games
    '''
    if tot_games != 0:
        return ('{0:.2f}'.format((wins/tot_games*100)) + "% win chance from " + str(wins) + " of " + str(tot_games) + " games")
    else:
        return "Will be first meeting"
    '''

'''
Returns calculate_win_pct given seed index and region
ex) vs_region(1,"EU") returns "X% win change vs EU" for CN2
'''
def vs_region(seed1,seed2):
# takes index and region right now
    seed2_to_cut = copy(seed2)
    region = seed2_to_cut[:-1]
    seed1_to_lookup = copy(seed1)
    index = find_index(seed1_to_lookup)
    
    if region == "CN":
        temp1 = copy(database[index][1])
        temp2 = copy(database[index][2])
        temp3 = copy(database[index][3])
        temp4 = condense(temp1,temp2)
        temp5 = condense(temp4,temp3)
    elif region == "EU":
        temp1 = copy(database[index][4])
        temp2 = copy(database[index][5])
        temp3 = copy(database[index][6])
        temp4 = condense(temp1,temp2)
        temp5 = condense(temp4,temp3)
    elif region == "KR":
        temp1 = copy(database[index][7])
        temp2 = copy(database[index][8])
        temp3 = copy(database[index][9])
        temp4 = condense(temp1,temp2)
        temp5 = condense(temp4,temp3)
    elif region == "LMS":
        temp1 = copy(database[index][10])
        temp2 = copy(database[index][11])
        temp3 = copy(database[index][12])
        temp4 = condense(temp1,temp2)
        temp5 = condense(temp4,temp3)
    elif region == "NA":
        temp1 = copy(database[index][13])
        temp2 = copy(database[index][14])
        temp3 = copy(database[index][15])
        temp4 = condense(temp1,temp2)
        temp5 = condense(temp4,temp3)
    elif region == "SEA":
        temp5 = copy(database[index][16])
    elif region == "TR":
        temp5 = copy(database[index][17])
    elif region == "VCS":
        temp5 = copy(database[index][18])
    elif region == "BR":
        temp5 = copy(database[index][19])
    elif region == "CIS":
        temp5 = copy(database[index][20])
    else:
        return 0.5
    # return test_actual(calculate_win_pct(temp5)*100)
    return calculate_win_pct(temp5)


'''
ways to calculate:
    1) if direct history exists (is not 0-0), given the win%, calculate actual win% (run odds 100,000 times)
        if that win% is (0% or 100%, change to 5% and 95% and calculate actual win%)
    2) average 1 with seed vs opponent region actual win% (0 and 100 fixed)
    3) average 1 with seed region vs opponent region actual win% (0 and 100 fixed)

'''
def test_actual(percent):
    temp = copy(percent)
    if temp == 100:
        temp = 98
    elif temp == 0:
        temp = 2
    wins = 0
    losses = 0
    for i in range(100000):
        rand = secrets.randbelow(100)
        if (rand <= temp):
            wins += 1
        elif (rand > temp):
            losses += 1
    return (wins/(wins+losses))
#actual = test100(100)
#print(actual)

'''
Given two seeds matched up, calculates win% based on direct history.
If the direct history is 100% for one seed winning against another, then calculations are adjusted to 98%, same for 0% to 2%.
'''
def direct(seed1,seed2):
    temp = copy(database[find_index(seed1)][find_index_opponent(seed2)])
    # multiply score by 100 if using in test_actual
    score = calculate_win_pct(temp)
    #actual = test_actual(score)
    return score

'''
Given two seeds matched up, calculates win% based on direct history,
    and averages that with the win% of seed1 vs seed2's region.
If the direct history is 100% for one seed winning against another, then calculations are adjusted to 98%, same for 0% to 2%. 
'''
def direct_and_region(seed1,seed2):
    temp = direct(seed1,seed2)
    '''
    seed2_short = copy(seed2)
    seed2_short = seed2_short[:-1]
    temp2 = vs_region(find_index(seed1), seed2_short)
    '''
    temp2 = vs_region(seed1,seed2)
    return (temp+temp2)/2


'''
    print("Group B: KR3, CN1, NA3, EU2")
    print("Group C: KR1, CN3, NA1, LMS2")
    print("Group D: EU1, CN2, NA2, LMS3")
'''

"""
print("---------------------------------")
print("Group A: KR2, LMS1, VCS1, EU3")
print("Testing...")
print("Direct, KR2 vs LMS1: "+str(direct("KR2","LMS1")))
print("KR2 vs LMS: "+str(vs_region("KR2","LMS1")))
print("Average of those two: "+str(direct_and_region("KR2","LMS1")))
print("Direct, LMS1 vs KR2: "+str(direct("LMS1","KR2")))
print("LMS1 vs KR: "+str(vs_region("LMS1","KR2")))
print("Average of those two: "+str(direct_and_region("LMS1","KR2")))
print("---------------------------------")
"""

print(str(direct("KR1","KR2")))
print(str(vs_region("KR1","KR2")))
print(str(direct_and_region("KR1","KR2")))
print(str(direct("KR2","KR1")))
print(str(vs_region("KR2","KR1")))
print(str(direct_and_region("KR2","KR1")))
