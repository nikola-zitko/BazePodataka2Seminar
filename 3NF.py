import itertools
def convertTuple(tup):
    str =  ''.join(tup)
    return str

def checkForm(R, Fmin, K):
    for fo in Fmin:
        isValid = True
        leftSide, rightSide = fo.split('->')
        #Prvi uvjet
        for att in rightSide:
            if att not in leftSide:
                isValid = False

        if isValid:
            continue

        #Drugi uvjet
        for temp_k in K:
            isValid = True
            for att in temp_k:
                if att not in leftSide:
                    isValid = False

            if isValid:
                break

        if isValid:
            continue

        #Treci uvjet
        for temp_k in K:
            isValid = True
            for att in rightSide:
                if att not in temp_k:
                    #Zadnji uvjet pa ako on nije ispunjen mozemo odmah vratit False
                    isValid = False

            if isValid:
                break

        if not isValid:
            return False

    return True

def normalize(R, Fmin):
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
    keyIncluded = False
    for key in K:
        key = ''.join(sorted(key))
        for fo in Fmin:
            fo = ''.join(sorted(set(fo.split('->'))))
            if key in fo:
                keyIncluded = True
                break

        if keyIncluded:
            print('Kljuc je vec ukljucen, a on je: ' + key)
            break
            
    if not keyIncluded:
        noviR.append(K[0])

    return noviR

R = "ABCDEF"
Fmin = ["A->B", "A->CD", "A->C", "C->BF", "E->BD"]
K=["A", "B", "C", "E"]

if checkForm(R, Fmin, K):
    print("Vec je u 3. NF")
else:
    print(normalize(R, Fmin))
