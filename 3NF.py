import itertools
def convertTuple(tup): 
    str =  ''.join(tup) 
    return str


R = "ABCDEF"
Fmin = ["A->B", "A->CD", "A->C", "C->BF", "E->BD"]
K=["A", "B", "C", "E"]
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

jel_treba_normlizirati = False
for fo in Fmin:
    dobar = True
    x,y=fo.split('->')
    #Prvi uvjet
    for att in y:
        if att not in x:
            dobar = False
    
    #Drugi uvjet
    if not dobar:
        for temp_k in K:
            dobar = True
            for att in temp_k:
                if att not in x:
                    dobar = False
            if dobar:
                break
            
        #Treci uvjet
        if not dobar:
            for temp_k in K:
                dobar = True
                for att in y:
                    if att not in temp_k:
                        dobar = False
                if dobar:
                    break
    #Provjera jel oke
    if not dobar:
        jel_treba_normlizirati = True

if not jel_treba_normlizirati:
    print("Vec je u 3. NF")

noviR=[]

for fo in Fmin:
    fo = ''.join(set(fo.split('->')))
    isIncluded = False
    for temp_R in noviR:
        isIncluded = True
        for att in fo:
            if att not in temp_R:
                isIncluded = False
        if isIncluded:
            break
    
    if not isIncluded:
        noviR.append(fo)

#Dodaj kljuc ako ga vec nema
sadrziKljuc = False
for kljuc in K:
    kljuc = ''.join(sorted(kljuc))
    for fo in Fmin:
        fo = ''.join(sorted(set(fo.split('->'))))
        if kljuc in fo:
            sadrziKljuc = True
            break
    if sadrziKljuc:
        print('Kljuc je vec ukljucen, a on je: ' + kljuc)
        break
if not sadrziKljuc:
    noviR.append(K[0])
    
print(noviR)