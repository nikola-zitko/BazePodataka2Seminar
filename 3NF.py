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
    newR=[]
    for fo in Fmin:
        originalFO = fo
        fo = ''.join(set(fo.split('->')))
        isIncluded = False
        for temp_R in newR:
            isIncluded = True
            for att in fo:
                if att not in temp_R:
                    isIncluded = False

            if isIncluded:
                print(originalFO + " je ukljucen u " + temp_R)
                break

        if not isIncluded:
            print(originalFO + " nije ukljucen, pa ga dodajemo.")
            newR.append(fo)
    print()

    #Dodaj kljuc ako ga vec nema
    for key in K:
        for fo in Fmin:
            keyIncluded = True
            fo = ''.join(set(fo.split('->')))
            for att in key:
                if att not in fo:
                    keyIncluded = False
                    break

            if keyIncluded:
                print('Kljuc ' + key + ' je vec ukljucen.')
                return newR

    print('Ni jedan kljuc nije ukljucen pa dodajemo kljuc: ' + K[0])
    newR.append(K[0])
    return newR

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

    print('Operacije su "Dodaj", "Izbrisi" i "Pokreni".')
    userChoice = input("Upisite zeljenu operaciju: ")
    if (userChoice.lower() == "dodaj"):
        #Unos
        userR = input("Unestite R: ").upper()
        userFmin = []
        userKeys= []
        while(True):
            userFminInput1 = input("Unesite lijevu stranu FO ili kraj za kraj unosa: ")
            if userFminInput1.lower() == "kraj":
                break
            userFminInput2 = input("Unesite desnu stranu FO: ")
            userFmin.append(userFminInput1 + '->' + userFminInput2)

        while(True):
            userKeyInput = input("Unesite kljuc ili kraj za kraj unosa: ")
            if userKeyInput.lower() == "kraj":
                break
            userKeys.append(userKeyInput)
        R.append(userR)
        Fmin.append(userFmin)
        K.append(userKeys)

    elif (userChoice.lower() == "izbrisi"):
        #Brisanje izabranog elemenata
        isValidInput = False;
        while not isValidInput:
            izbor=int(input("Unesite broj RS koje zelite izbrisati: "))
            if (izbor > 0 and izbor <= len(R)):
                izbor -= 1
                isValidInput = True
            else:
                print("Unesite ispravan broj.")

        del R[izbor]
        del Fmin[izbor]
        del K[izbor]

    elif (userChoice.lower() == "pokreni"):
        for i in range(len(R)):
            print(str(i + 1) + ".\n" +
            "R: " + R[i]+ "\n" +
            "Fmin: " + ', '.join(Fmin[i]) +
            "\nK: " + ', '.join(K[i]) + "\n")
            if checkForm(R[i], Fmin[i], K[i]):
                print("\nVec je u 3. NF")

            else:
                print()
                print('Novi R je: ' + ', '.join(normalize(R[i], Fmin[i], K[i])))

            print()
        break

    elif (userChoice.lower() == "kraj"):
        break

    else:
        print("Unesite valjdanu operaciju.")
