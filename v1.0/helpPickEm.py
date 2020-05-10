import csv
from copy import copy

# TAKES DATASET FROM 2017 WC GAMES, PULLS TEAM NAMES AND RESULTS
games = []
with open('/Users/GakuSasaki/Documents/python workspace/helpPickEm/data/wc2017.csv', 'r') as file:
    reader = csv.reader(file)
    rowNr = 0
    for row in reader:
        if rowNr >= 1:
            games.append([[row[4], row[5], row[6],row[7]]])  
        rowNr = rowNr + 1
file.close()
# at this point, games looks like [['bTeam', 'bResult', 'rResult', 'rTeam']]


# ADDS REGION AND SEEDING TAGS TO EACH TEAM
seeding = []
with open('/Users/GakuSasaki/Documents/python workspace/helpPickEm/data/seeding.csv', 'r') as file:
    reader = csv.reader(file)
    rowNr = 0
    for row in reader:
        if rowNr >= 1:
            seeding.append([row[0],row[1],row[2]])
        rowNr = rowNr + 1
file.close()
# at this point, seeding looks like [['region', 'seed', 'team']]
for game in games:
    for seed in seeding:
        if game[0][0] == seed[2]:
            game[0] = [seed[0],seed[1]] + game[0]
    for seed in seeding:
        if game[0][5] == seed[2]:
            game[0] = game[0] + [seed[1],seed[0]]

# USING DATA, CREATES CSV OF TEAM NAMES, RESULTS
csvheader = [['bRegion','bSeed','bTeam', 'bResult', 'rResult', 'rTeam', 'rSeed', 'rRegion']]
with open('WC2017_teamsandresultsonly.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvheader)
    rowNr = 0
    for game in games:
        writer.writerows(games[rowNr])
        rowNr += 1
csvFile.close()

# at this point, games looks like  [['bRegion','bSeeding','bTeam', 'bResult', 'rResult', 'rTeam','rSeeding','rRegion']]
# ---------------------------------------------------------------------------------------------------
'''
somewhere should consider GROUPS ONLY version and OVERALL version.
'''


csvheader = [['Region','Seed','vsBR1','vsCN1','vsCN2','vsCN3','vsCIS1','vsEU1','vsEU2','vsEU3','vsJP1',
              'vsKR1','vsKR2','vsKR3','vsLAN1','vsLAS1','vsLMS1','vsLMS2','vsLMS3','vsNA1','vsNA2','vsNA3',
              'vsOCE1','vsSEA1','vsSEA2','vsTR1','vsTW1','vsTW2']]
template = ['region',1,
['BR',1,0,0],['CN',1,0,0],['CN',2,0,0],['CN',3,0,0],['CIS',1,0,0],['EU',1,0,0],['EU',2,0,0],
['EU',3,0,0],['JP',1,0,0],['KR',1,0,0],['KR',2,0,0],['KR',3,0,0],['LAN',1,0,0],['LAS',1,0,0],
['LMS',1,0,0],['LMS',2,0,0],['LMS',3,0,0],['NA',1,0,0],['NA',2,0,0],['NA',3,0,0],['OCE',1,0,0],
['SEA',1,0,0],['SEA',2,0,0],['TR',1,0,0],['TW',1,0,0],['TW',2,0,0]]


'''
RETURNS database = a list of items and lists
formatted with the template.
'''
def create_database(template):
    database = []

#BR 1
    br1 = copy(template)
    br1[0] = 'BR'
    database.append(br1)
#CN 1-3
    cn1 = copy(template)
    cn1[0] = 'CN'
    database.append(cn1)
    cn2 = copy(template)
    cn2[0] = 'CN'
    cn2[1] = 2
    database.append(cn2)
    cn3 = copy(template)
    cn3[0] = 'CN'
    cn3[1] = 3
    database.append(cn3)
#CIS 1
    cis1 = copy(template)
    cis1[0] = 'CIS'
    database.append(cis1)
#EU 1-3
    eu1 = copy(template)
    eu1[0] = 'EU'
    database.append(eu1)
    eu2 = copy(template)
    eu2[0] = 'EU'
    eu2[1] = 2
    database.append(eu2)
    eu3 = copy(template)
    eu3[0] = 'EU'
    eu3[1] = 3
    database.append(eu3)
#JP 1
    jp1 = copy(template)
    jp1[0] = 'JP'
    database.append(jp1)
#KR 1-3
    kr1 = copy(template)
    kr1[0] = 'KR'
    database.append(kr1)
    kr2 = copy(template)
    kr2[0] = 'KR'
    kr2[1] = 2
    database.append(kr2)
    kr3 = copy(template)
    kr3[0] = 'KR'
    kr3[1] = 3
    database.append(kr3) 
#LAN 1
    lan1 = copy(template)
    lan1[0] = 'LAN'
    database.append(lan1)
#LAS 1
    las1 = copy(template)
    las1[0] = 'LAS'
    database.append(las1)
#LMS 1-3
    lms1 = copy(template)
    lms1[0] = 'LMS'
    database.append(lms1)
    lms2 = copy(template)
    lms2[0] = 'LMS'
    lms2[1] = 2
    database.append(lms2)
    lms3 = copy(template)
    lms3[0] = 'LMS'
    lms3[1] = 3
    database.append(lms3)
#NA 1-3
    na1 = copy(template)
    na1[0] = 'NA'
    database.append(na1)
    na2 = copy(template)
    na2[0] = 'NA'
    na2[1] = 2
    database.append(na2)
    na3 = copy(template)
    na3[0] = 'NA'
    na3[1] = 3
    database.append(na3)
#OCE 1
    oce1 = copy(template)
    oce1[0] = 'OCE'
    database.append(oce1)
#SEA 1-2
    sea1 = copy(template)
    sea1[0] = 'SEA'
    database.append(sea1)
    sea2 = copy(template)
    sea2[0] = 'SEA'
    sea2[1] = 2
    database.append(sea2)
#TR 1
    tr1 = copy(template)
    tr1[0] = 'TR'
    database.append(tr1)
#TW 1-2
    tw1 = copy(template)
    tw1[0] = 'TW'
    database.append(tw1)
    tw2 = copy(template)
    tw2[0] = 'TW'
    tw2[1] = 2
    database.append(tw2)
    return database


'''
VOID, Adds one row to the database.
assume row is formatted as [['bRegion','bSeeding','bTeam', 'bResult', 'rResult', 'rTeam','rSeeding','rRegion']]
assume database is formatted as a list of seeds

'''
def update(database,row):
    
    for seed in database:
        print("starting execute for " + str(seed[0])+str(seed[1]))
        print("checking KR2: " + str(seed[12]))
        
        if seed[0] == row[0][0] and seed[1] == int(row[0][1]):
            if row[0][3] == "1" and row[0][4] == "0":
                for item in seed:
                    if type(item) == list and item[0] == row[0][7] and item[1] == int(row[0][6]):
                        item[2] += 1 
            elif row[0][3] == "0" and row[0][4] == "1":
                for item in seed:
                    if type(item) == list and item[0] == row[0][7] and item[1] == int(row[0][6]):
                        item[3] += 1
        elif seed[0] == row[0][7] and seed[1] == int(row[0][6]):  
            if row[0][3] == "1" and row[0][4] == "0":
                for item in seed:
                    if type(item) == list and item[0] == row[0][0] and item[1] == int(row[0][1]):
                        item[3] += 1 
            elif row[0][3] == "0" and row[0][4] == "1":
                for item in seed:
                    if type(item) == list and item[0] == row[0][0] and item[1] == int(row[0][1]):
                        item[2] += 1

        print("finished execute for " + str(seed[0])+str(seed[1]))
        print("checking KR2: " + str(seed[12])+"\n")




row = [['NA', '3', 'C9', '0', '1', 'SKT','2','KR']]

toWrite = create_database(template)
update(toWrite,row)
print(toWrite[0][12])


with open('seeds_database.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvheader)
    for seed in toWrite:
        writer.writerows([seed])
csvFile.close()




print('{0:.2f}'.format((5 / 6 * 100)))
