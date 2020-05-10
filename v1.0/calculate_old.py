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
    if tot_games != 0:
        return ('{0:.2f}'.format((wins/tot_games*100)) + "% win chance from " + str(wins) + " of " + str(tot_games) + " games")
    else:
        return "Will be first meeting"

'''
Returns calculate_win_pct given seed index and region
ex) vs_region(1,"EU") returns "X% win change vs EU" for CN2
'''
def vs_region(index,region):
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
    else:
        return "Region never had multiple seeds in groups or further."
    return calculate_win_pct(temp5) + " vs " + region


# Group A
def groupA():
    print("-----------------------------------------------")
    print("Group A: KR2, LMS1, VCS1, EU3")
    print("-----------------------------------------------")
    print("KR2")
    print(" vs LMS1")
    print(calculate_win_pct(str(database[7][10])))
    print(vs_region(7,"LMS"))
    print(" vs VCS1")
    print(calculate_win_pct(str(database[7][18])))
    print(" vs EU3")
    print(calculate_win_pct(str(database[7][6])))
    print(vs_region(7,"EU"))
    print("-----------------------------------------------")
    print("LMS1")
    print("vs KR2")
    print(calculate_win_pct(str(database[9][8])))
    print(vs_region(9,"KR"))
    print("vs VCS1")
    print(calculate_win_pct(str(database[9][18])))
    print("vs EU3")
    print(calculate_win_pct(str(database[9][6])))
    print(vs_region(9,"EU"))
    print("-----------------------------------------------")
    print("VCS1")
    print("vs KR2")
    print(calculate_win_pct(str(database[17][8])))
    print("vs LMS1")
    print(calculate_win_pct(str(database[17][10])))
    print("vs EU3")
    print(calculate_win_pct(str(database[17][6])))
    print("-----------------------------------------------")
    print("EU3")
    print("vs KR2")
    print(calculate_win_pct(str(database[5][8])))
    print(vs_region(5,"KR"))
    print("vs LMS1")
    print(calculate_win_pct(str(database[5][10])))
    print(vs_region(5,"LMS"))
    print("vs VCS1")
    print(calculate_win_pct(str(database[5][18])))


# Group B
def groupB():
    print("-----------------------------------------------")
    print("Group B: KR3, CN1, NA3, EU2")
    print("-----------------------------------------------")
    print("KR3")
    print(" vs CN1")
    print(calculate_win_pct(str(database[8][1])))
    print(" vs NA3")
    print(calculate_win_pct(str(database[8][15])))
    print(" vs EU2")
    print(calculate_win_pct(str(database[8][5])))
    print("-----------------------------------------------")
    print("CN1")
    print(" vs KR3")
    print(calculate_win_pct(str(database[0][9])))
    print(" vs NA3")
    print(calculate_win_pct(str(database[0][15])))
    print(vs_region(0,"NA"))
    print(" vs EU2")
    print(calculate_win_pct(str(database[0][5])))
    print(vs_region(0,"EU"))

    print("-----------------------------------------------")
    print("NA3")
    print(" vs KR3")
    print(calculate_win_pct(str(database[14][9])))
    print(" vs CN1")
    print(calculate_win_pct(str(database[14][1])))
    print(vs_region(14,"CN"))
    print(" vs EU2")
    print(calculate_win_pct(str(database[14][5])))
    print(vs_region(14,"EU"))

    print("-----------------------------------------------")
    print("EU2")
    print(" vs KR3")
    print(calculate_win_pct(str(database[4][9])))
    print(" vs CN1")
    print(calculate_win_pct(str(database[4][1])))
    print(vs_region(4,"CN"))
    print(" vs NA3")
    print(calculate_win_pct(str(database[4][15])))
    print(vs_region(4,"NA"))


# Group C
def groupC():
    print("-----------------------------------------------")
    print("Group C: KR1, CN3, NA1, LMS2")
    print("-----------------------------------------------")
    print("KR1")
    print(" vs CN3")
    print(calculate_win_pct(str(database[6][3])))
    print(" vs NA1")
    print(calculate_win_pct(str(database[6][13])))
    print(" vs LMS2")
    print(calculate_win_pct(str(database[6][11])))
    print(vs_region(6,"LMS"))
    print("-----------------------------------------------")
    print("CN3")
    print(" vs KR1")
    print(calculate_win_pct(str(database[2][7])))
    print(" vs NA1")
    print(calculate_win_pct(str(database[2][13])))
    print(" vs LMS2")
    print(calculate_win_pct(str(database[2][11])))
    print(vs_region(2,"LMS"))
    print("-----------------------------------------------")
    print("NA1")
    print(" vs KR1")
    print(calculate_win_pct(str(database[12][7])))
    print(" vs CN3")
    print(calculate_win_pct(str(database[12][3])))
    print(vs_region(12,"CN"))
    print(" vs LMS2")
    print(calculate_win_pct(str(database[12][11])))
    print(vs_region(12,"LMS"))
    print("-----------------------------------------------")
    print("LMS2")
    print(" vs KR1")
    print(calculate_win_pct(str(database[10][7])))
    print(vs_region(10,"KR"))
    print(" vs CN3")
    print(calculate_win_pct(str(database[10][3])))
    print(vs_region(10,"CN"))
    print(" vs NA1")
    print(calculate_win_pct(str(database[10][13])))
    print(vs_region(10,"NA"))

# Group D
def groupD():
    print("-----------------------------------------------")
    print("Group D: EU1, CN2, NA2, LMS3")
    print("-----------------------------------------------")
    print("EU1")
    print(" vs CN2")
    print(calculate_win_pct(str(database[3][2])))
    print(" vs NA2")
    print(calculate_win_pct(str(database[3][14])))
    print(" vs LMS3")
    print(calculate_win_pct(str(database[3][12])))
    print(vs_region(6,"LMS"))
    print("-----------------------------------------------")
    print("CN2")
    print(" vs EU1")
    print(calculate_win_pct(str(database[1][4])))
    print(" vs NA2")
    print(calculate_win_pct(str(database[1][14])))
    print(" vs LMS3")
    print(calculate_win_pct(str(database[1][12])))
    print(vs_region(2,"LMS"))
    print("-----------------------------------------------")
    print("NA2")
    print(" vs EU1")
    print(calculate_win_pct(str(database[13][4])))
    print(" vs CN2")
    print(calculate_win_pct(str(database[13][2])))
    print(vs_region(12,"CN"))
    print(" vs LMS3")
    print(calculate_win_pct(str(database[13][12])))
    print(vs_region(12,"LMS"))
    print("-----------------------------------------------")
    print("LMS3")
    print(" vs EU1")
    print(calculate_win_pct(str(database[9][4])))
    print(vs_region(10,"KR"))
    print(" vs CN2")
    print(calculate_win_pct(str(database[9][2])))
    print(vs_region(10,"CN"))
    print(" vs NA2")
    print(calculate_win_pct(str(database[9][14])))
    print(vs_region(10,"NA"))






