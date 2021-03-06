import csv
import copy
'''
only groups.

TEMPLATE = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})


INDEX LIST
{"CN1":"0-0"} = 0
{"CN2":"0-0"} = 1
{"CN3":"0-0"} = 2
{"EU1":"0-0"} = 3
{"EU2":"0-0"} = 4
{"EU3":"0-0"} = 5
{"KR1":"0-0"} = 6
{"KR2":"0-0"} = 7
{"KR3":"0-0"} = 8
{"LMS1":"0-0"} = 9
{"LMS2":"0-0"} = 10
{"LMS3":"0-0"} = 11
{"NA1":"0-0"} = 12
{"NA2":"0-0"} = 13
{"NA3":"0-0"} = 14
{"SEA1":"0-0"} = 15
{"TR1":"0-0"} = 16
{"VCS1":"0-0"} = 17


'''
# database everything.
og_CN1 = [{"CN1":""},{"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},{"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"}]
og_CN2 = [{"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},{"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"}]
og_CN3 = [{"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},{"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"}]
og_EU1 = [{"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},{"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"}]
og_EU2 = [{"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},{"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"}]
og_EU3 = [{"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},{"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"}]
og_KR1 = [{"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},{"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"}]
og_KR2 = [{"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},{"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"}]
og_KR3 = [{"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},{"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"}]
og_LMS1 = [{"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},{"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"}]
og_LMS2 = [{"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},{"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"}]
og_LMS3 = [{"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},{"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"}]
og_NA1 = [{"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},{"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"}]
og_NA2 = [{"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},{"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"}]
og_NA3 = [{"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},{"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"}]
og_SEA1 = [{"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},{"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"}]
og_TR1 = [{"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},{"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"}]
og_VCS1 = [{"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},{"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"}]
database = [og_CN1,og_CN2,og_CN3,og_EU1,og_EU2,og_EU3,og_KR1,og_KR2,og_KR3,og_LMS1,
            og_LMS2,og_LMS3,og_NA1,og_NA2,og_NA3,og_SEA1,og_TR1,og_VCS1]
'''
def consolidate(toAdd):
    temp = copy(toAdd)
    if len(temp1) == len(temp):
        for dicti in temp1:
            print(dicti.key())
            # if dict key is equal
                # add values together
            
    return ans
''' 



# 2017 GROUP A
KR2 = ({"CN1":"2-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"1-1"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"2-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})
NA3 = ({"CN1":"1-1"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-2"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"2-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})
LMS2 = ({"CN1":"1-1"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"1-1"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-2"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})
CN1 = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-2"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"1-1"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"1-1"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})

# 2017 GROUP B
KR1 = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"2-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"2-0"},{"NA3":"0-0"},{"SEA1":"2-0"},{"TR1":"0-0"},{"VCS1":"0-0"})
EU3 = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-2"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"2-1"},{"NA3":"0-0"},{"SEA1":"2-1"},{"TR1":"0-0"},{"VCS1":"0-0"})
SEA1 = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"1-2"},{"KR1":"0-2"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"1-1"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})
NA2 = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"1-2"},{"KR1":"0-2"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"1-1"},{"TR1":"0-0"},{"VCS1":"0-0"})


# 2017 GROUP C
CN2 = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"1-1"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"2-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"2-0"},{"VCS1":"0-0"})
KR3 = ({"CN1":"0-0"},{"CN2":"0-2"},{"CN3":"0-0"},{"EU1":"2-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"2-0"},{"VCS1":"0-0"})
EU1 = ({"CN1":"0-0"},{"CN2":"1-1"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-2"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"2-0"},{"VCS1":"0-0"})
TR1 = ({"CN1":"0-0"},{"CN2":"0-2"},{"CN3":"0-0"},{"EU1":"0-2"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-2"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})

# 2017 GROUP D
CN3 = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"2-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"2-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"1-1"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})
EU2 = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-2"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"2-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"2-1"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})
NA1 = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"1-1"},{"EU1":"0-0"},{"EU2":"1-2"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"1-1"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})
LMS1 = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-2"},{"EU1":"0-0"},{"EU2":"0-2"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"1-1"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})

# 2017 BRACKET
KR2_1 = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"3-2"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})
EU2_1 = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"2-3"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})
CN2_1= ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"3-1"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})
EU3_1 = ({"CN1":"0-0"},{"CN2":"1-3"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})
CN3_1 = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"3-2"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})
NA3_1 = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"2-3"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})
KR1_1 = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-3"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})
KR3_1 = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"3-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})
KR2_2 = ({"CN1":"0-0"},{"CN2":"3-2"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})
CN2_2 = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"2-3"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})
CN3_2 = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"1-3"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})
KR3_2 = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"3-1"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})
KR2_3 = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"0-0"},{"KR3":"0-3"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})
KR3_3 = ({"CN1":"0-0"},{"CN2":"0-0"},{"CN3":"0-0"},{"EU1":"0-0"},{"EU2":"0-0"},{"EU3":"0-0"},{"KR1":"0-0"},{"KR2":"3-0"},{"KR3":"0-0"},{"LMS1":"0-0"},{"LMS2":"0-0"},{"LMS3":"0-0"},
    {"NA1":"0-0"},{"NA2":"0-0"},{"NA3":"0-0"},{"SEA1":"0-0"},{"TR1":"0-0"},{"VCS1":"0-0"})



GROUPA2017 = [KR2,NA3,LMS2,CN1]
GROUPB2017 = [KR1,EU3,SEA1,NA2]
GROUPC2017 = [CN2,KR3,EU1,TR1]
GROUPD2017 = [CN3,EU2,NA1,LMS1]
BRACKET2017 = [KR2_1,EU2_1,CN2_1,EU3_1,CN3_1,NA3_1,KR1_1,KR3_1,KR2_2,CN2_2,CN3_2,KR3_2,KR2_3,KR3_3]





# 2018 GROUP A
# AFREECA,FW,PHONG VU, G2
# KR2,LMS1,VCS1,EU3

# 2018 GROUP B
# GENG,RNG,C9,VIT
# KR3,CN1,NA3,EU2
'''
print("KR3: "+str(KR3[0])+str(KR3[14])+str(KR3[4]))
print("CN1: "+str(KR3[8])+str(KR3[14])+str(KR3[4]))
print("NA3: "+str(KR3[0])+str(KR3[8])+str(KR3[4]))
print("EU2: "+str(KR3[0])+str(KR3[8])+str(KR3[14]))
'''


# 2018 GROUP C
# KT,EDG,TL,MAD
# KR1,CN3,NA1,LMS2

# 2018 GROUP D
# FNC,INV,100,GREX
# EU1,CN2,NA2,LMS3




csvheader = [['seed','CN1','CN2','CN3','EU1','EU2','EU3','KR1','KR2','KR3',
              'LMS1','LMS2','LMS3','NA1','NA2','NA3','SEA1','TR1','VCS1']]
with open('db.csv','w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvheader)
    rowNr = 0
    for seed in database:
        writer.writerows(database[rowNr])
        rowNr += 1
    print(rowNr)
csvFile.close()
