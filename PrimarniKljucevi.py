import itertools
def mainmenu():
    print("___________________")
    print("____Baze Podataka 2____")
    print("1. Unesite relacijsku shema")
    print("2. Racunanje primarnog kljuca")
    
def addFmin(Fmin, fo):
    Fmin.append(fo)

def convertTuple(tup): 
    str =  ''.join(tup) 
    return str


R = "ABCDEF"
Fmin = ["A->B", "A->C", "B->AECD", "C->BF", "E->BD"]
canonical_form = []
for att in Fmin:
    x = att.split('->')
    if(len(x[1])>1):
        for z in x[1]:
            canonical_form.append(x[0] + "->" + z)
    else:
        canonical_form.append(att)

print(Fmin)
print(canonical_form)

L = []
#D = []
for FO in Fmin:
    livi = (FO.split('->'))[0]
    desni = (FO.split('->'))[1]

    for att in livi:
        if att not in L:
            L.append(att)
    """for att in desni:
        if att not in D:
            D.append(att)
    """
print(L)


potential_key_candidates = []

for att in range(1, len(L)+1):
    for subset in itertools.combinations(L, att):
        potential_key_candidates.append(convertTuple(subset))
print("Key candidates: " + ', '.join(potential_key_candidates))

K = []
tmp = []
for potential_candidate in potential_key_candidates: #moguci kandidati
    temp = potential_candidate
    isUpdated = True
    while(isUpdated):
        isUpdated = False
        for attribute in temp: #Svako slovo posebno
            for f_dependency in canonical_form: #FO
                if(attribute == f_dependency.split('->')[0]):
                    if f_dependency.split('->')[1] not in temp:
                        #tmp.append(f_dependency.split('->')[1])
                        temp = temp + f_dependency.split('->')[1]
                        isUpdated = True
                        print(temp)
                        if ''.join(sorted(temp)) == R:
                            K.append(potential_candidate)
                        
    print()
    

print(K)
for x in K:
    if(len(x) == len(K[0])):
        print(x)
    else:
        break

