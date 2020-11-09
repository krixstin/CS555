from datetime import datetime
from dateutil.relativedelta import relativedelta


def childbirths(famDICT,Indi_DICT):
    children = []
    children_birth = []
    birth_cond = True
    for fam in famDICT.values():
        for i in fam:
            if i[0] == 'CHIL':
                children.append(Indi_DICT.get(i[1]))
        for j in children:
            children_birth.append(datetime.strptime(j[2], "%d %b %Y"))
        for k in children_birth:
            for i in children_birth:
                if abs((k.year - i.year) * 12 + (k.month - i.month)) < 9 and abs((k - i).days) > 1:
                    birth_cond = False
        children_birth = []
        children = []
    return birth_cond
