#Unit Conversion Functions
#metric
def kilometersToMi(km, kmMiConFact):
    mi = km*kmMiConFact
    return mi

def degreesCToF(c, cConFact):
    f = (c*cConFact)+32
    return f

def litersToG(l, lGConFact):
    g = l/lGConFact
    return g

def kilogramsToLb(kg, kgLbConFact):
    lb = kg/kgLbConFact
    return lb

def centimetersToIn(cm, cmInConFact):
    iN = cm/cmInConFact
    return iN

#imperial
def milesToKm(mi, kmMiConFact):
    km = mi/kmMiConFact
    return km

def degreesFToC(f, fConFact):
    c = (f-32)*fConFact
    return c

def gallonsToL(g, lGConFact):
    l = g*lGConFact
    return l

def poundsToKg(lb, kgLbConFact):
    kg = lb*kgLbConFact
    return kg

def inchesToCm(iN, cmInConFact):
    cm = iN*cmInConFact
    return cm
