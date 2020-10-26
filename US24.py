def unique_spouses(famDICT):
    marrages = []
    date = []
    insertTag = False
    for items in famDICT.values():
        husb = items[0]
        wife = items[1]
        for i in items:
            if i == ['MARR']:
                insertTag = True
            elif insertTag:
                date = i
                insertTag = False
        marrages.append((husb[2], wife[2], date[1]))
    uniqueM = len(set(marrages)) == len(marrages)
    if uniqueM:
        return True
    else:
        return False
