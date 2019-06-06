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
            print("Za " + fo + " je prvi uvjet ispunjen.")
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
            print("Za " + fo + " je drugi uvjet ispunjen.")
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
            print("Za " + fo + " niti jedan uvjet nije ispunjen.")
            return False

    print("Za " + fo + " je treci uvjet ispunjen.")
    return True

def normalize(R, Fmin, K):
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
    #Neradi ako se redosljed ne podudara/Ima neki drugi att izmedu
    #Kako i gdje cemo spremat rezultate? Ili da ostane samo ispis novog R-a?
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

#Glavni program

R = ["ABC", "ABCD", "ABCDEF","ABCDEFG", "ABCDEF"]
Fmin = [["A->B","B->C"], ["AC->B", "C->D", "B->A"], ["A->B", "A->CD", "A->C", "C->BF", "E->BD"],
["A->D", "AG->B", "B->G", "B->E", "E->B", "E->F"], ["A->B", "CD->A", "CB->D", "CE->D", "AE->F"]]
K=[["A"], ["AC", "BC"], ["A", "B", "C", "E"], ["ACG", "ACB", "ACE"], ["CE"]]

print("Seminar iz Baza Podataka 2.\nNormalizacija u 3. Normalnu formu")
while(True):
    print()
    for i in range(len(R)):
        print(str(i + 1) + ".\n" +
        "R: " + R[i]+ "\n" +
        "Fmin: " + ', '.join(Fmin[i]) +
        "\nK: " + ', '.join(K[i]) + "\n")

    userChoice = input("Upisite zeljenu operaciju: ")
    if (userChoice.lower() == "dodaj"):
        pass #Unos

    elif (userChoice.lower() == "makni"):
        pass #Brisanje

    elif (userChoice.lower() == "izvedi"):
        for i in range(len(R)):
            print(str(i + 1) + ".\n" +
            "R: " + R[i]+ "\n" +
            "Fmin: " + ', '.join(Fmin[i]) +
            "\nK: " + ', '.join(K[i]) + "\n")
            if checkForm(R[i], Fmin[i], K[i]):
                print("Vec je u 3. NF")

            else:
                print(normalize(R[i], Fmin[i], K[i]))

            print()
        break

    elif (userChoice.lower() == "kraj"):
        break
