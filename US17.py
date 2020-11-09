def parentsNotMarriedToChildren(fam_dict):
    ids = []
    cond = True
    for fam in fam_dict.values():
        for i in fam:
            if i[0] == 'HUSB':
                ids.append(i[1])
            if i[0] == 'CHIL':
                ids.append(i[1])
            if i[0] == 'WIFE':
                ids.append(i[1])
        if len(ids) != len(set(ids)):
            cond = False;
        ids = []
    return cond



