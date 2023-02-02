Famille={"eve":{"tom","lea","luc","kim"},"tom":{"isa","bob"},"lea":{"ali"},"bob":{"bea","tim"},"luc":{"sam","jon","lou"},"sam":{"ana","guy"},"guy":{"ben"}}

def enfants(F,x):
    if x in F:
        return F.get(x)
    else:
        return set()

print(enfants(Famille,"eve"))

def enfants_ens(F,X):
    lee=set()
    for p in X:
        le=enfants(F,p)
        for e in le :
            lee.add(e)
    return lee

print(enfants_ens(Famille,{"tom","lea"}))

def petits_enfants(F,x):
    le=enfants(F,x)
    lpe=enfants_ens(F,le)
    return lpe

print(petits_enfants(Famille,"eve"))

def parents(F,x):
    lp=set()
    for p,le in F.items():
        if x in le:
            lp.add(p)
    return lp

print(parents(Famille,"lea"))

def freres_soeurs(F,x):
    lfs=set()
    lp=parents(F,x)
    for p in lp:
        for e in F[p]:
            if e is not x:
                lfs.add(e)
    return lfs

print(freres_soeurs(Famille,"lea"))

def neveux_nieces(F,x):
    lff=freres_soeurs(F,x)
    lnn=enfants_ens(F,lff)
    return lnn

print(neveux_nieces(Famille,"lea"))