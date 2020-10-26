import datetime
from dateutil.relativedelta import relativedelta

def birth_before_death(famDICT, INDI_DICT):
    children = []
    children_birth = []
    birth_before_death_Cond = True
    husbID = ''
    husbDeathDate = ''
    wifeID = ''
    wifeDeathDate = ''
    for items in famDICT.values():
        husb = items[0]
        husbID = husb[1]
        wife = items[1]
        wifeID = wife[1]
        for i in items:
            if i[0] == 'CHIL':
                children.append(INDI_DICT.get(i[1]))
        for j in children:
            children_birth.append(datetime.strptime(j[3],"%d/%m/%y"))
        print(children_birth)
        husbID = INDI_DICT.get(husbID)
        wifeID = INDI_DICT.get(wifeID)
        if wifeID[5]:
            wifeDeathDate = datetime.strptime(wifeID[6], "%d/%m/%y")
            for k in children_birth:
                if wifeDeathDate < k:
                    birth_before_death_Cond = False
        if husbID[5]:
            husbDeathDate = datetime.strptime(husbID[6], "%d/%m/%y")
            for i in children_birth:
                i + relativedelta(months=-6)
                if husbDeathDate < i:
                    birth_before_death_Cond = False
    return birth_before_death_Cond


