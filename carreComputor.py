def ft_sqrt(nb):
    ret = ""
    if nb < 0:
        return -1
    if nb == 0:
        return 0
    if nb == 1:
        return 1
    impair = 1
    tmp = 1
    countE = 1
    while (tmp + (impair + 2)) <= nb:
        impair += 2
        tmp += impair
        countE += 1
    reste = nb - tmp
    ret =  str(countE)
    if reste == 0:
        return countE
    
    ret += "."
    countD = 1
    toto = 0
    retrait = reste
    while toto < 10:
        countImpair = 0#KEEP
        impairSuivant = ((impair + 1) * 10) + 1#KEEP
        retrait = retrait * 100
        while (retrait - impairSuivant) > 0:
            retrait = retrait - impairSuivant
            impairSuivant += 2
            countImpair += 1
        ret += str(countImpair)#KEEP
        toto += 1
        impair = impairSuivant - 2
    return float(ret)

def ft_carre(nb):
    return nb * nb