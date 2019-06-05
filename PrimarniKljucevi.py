import itertools
def mainmenu(R,Fmin):
    print("___________________")
    print("____Baze Podataka 2____")
    for x in range(len(R)):
        print(str(x+1)+". R = "+R[x] + "; Fmin = " + ', '.join(Fmin[x]))

    
def addFmin(Fmin, fo):
    Fmin.append(fo)

def convertTuple(tup): 
    str =  ''.join(tup) 
    return str



R = ["ABCD","ABCDE","ABCDEFGH","AB","ABCDE","ABCDEF","ABC","ABCDEFGHI","ABCDE","ABCD"]
Fmin = [["A->B", "A->C"],["AB->D","B->E","C->AB"],["AB->E","C->FG","E->AH"],["A->A","A->B","B->A","B->B"],["A->BC","C->E","D->E","B->D"],
["A->BCD","B->E","C->DEF","EF->BD"],["A->B","C->AB","B->BC"],["A->BCD","BC->ADE","FAG->A","EF->G","F->A"],["A->E","B->D","C->C","E->AB"],["A->A","B->B","C->C","D->D","ABCD->ABCD"]]
canonical_form = []

mainmenu(R, Fmin)
odabir = int(input("Unesite broj R sheme: "))

Fmin = Fmin[odabir-1]
R = R[odabir-1]

for att in Fmin:
    x = att.split('->')
    if(len(x[1])>1):
        for z in x[1]:
            canonical_form.append(x[0] + "->" + z)
    else:
        canonical_form.append(att)

print(Fmin)
print(canonical_form)

RodF = ""
for att in canonical_form:
    x = att.split('->')
    if(x[0] not in RodF):
        RodF = RodF + x[0]
    if(x[1] not in RodF):
        RodF = RodF + x[1]

print("RodF je ")
RodF = ''.join(sorted(RodF))
print(RodF)

K1 = R
K1=K1.replace(RodF,'')

R = R.replace(K1,'')

print(K1)


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
                        
                        if ''.join(sorted(temp)) == R:
                            
                            K.append(potential_candidate+K1)
                            
                        
    
    

print(K)
for x in K:
    if(len(x) == len(K[0])):
        print(x)
    else:
        break

