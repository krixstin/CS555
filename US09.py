from datetime import datetime
import dateutil.relativedelta

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
            children_birth.append(datetime.strptime(j[2], "%d %b %Y"))
        print(children_birth)
        husbID = INDI_DICT.get(husbID)
        wifeID = INDI_DICT.get(wifeID)
        if not wifeID[4]:
            wifeDeathDate = datetime.strptime(wifeID[5], "%d %b %Y")
            for k in children_birth:
                if wifeDeathDate < k:
                    birth_before_death_Cond = False
        if not husbID[4]:
            husbDeathDate = datetime.strptime(husbID[5], "%d %b %Y")
            for i in children_birth:
                i - dateutil.relativedelta.relativedelta(months=9)
                if husbDeathDate < i:
                    birth_before_death_Cond = False
        children = []
        children_birth = []
    return birth_before_death_Cond


