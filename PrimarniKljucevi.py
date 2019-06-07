import itertools
def mainmenu(R,Fmin):
    print("_______________________")
    print("____Baze Podataka 2____")
    for x in range(len(R)):
        print(str(x+1)+". R = "+R[x] + "; Fmin = " + ', '.join(Fmin[x]))
    print(str(len(R)+1) + ". Unos nove relacijske sheme i skupa F.O.")
    print(str(len(R)+2) + ". Brisanje R i F.O.")
    print(str(len(R)+3) + ". Izlaz iz programa!")
    

def unosNovog(R, Fmin):
    novaFO = []
    noviR = input("Unesite novu relacijsku shemu:")
    brojFO = int(input("Unesite broj funkcijskih ovisnosti:"))
    for x in range (brojFO):
        novaFO.append(input("Unesite " + str(x+1) + ". FO:"))
    Fmin.append(novaFO)
    R.append(noviR)
    return R, Fmin

def brisanje(R, Fmin):
    broj = int(input("Unesite redni broj relacije koju zelite izbrisati: "))
    broj = broj-1
    if(broj>=0 and broj<len(R)):
        R.pop(broj)
        Fmin.pop(broj)
    return R, Fmin


def convertTuple(tup): 
    str =  ''.join(tup) 
    return str


#"U svakoj shemi se nalazi minimalno deset atributa i minimalno pet funkcionalnih ovisnosti"
R = ["ABCDEFGHIJ","ABCDEFGHIJK","ABCDEFGHIJKLMNO","ABCDEFGHIJKLMNOP","ABCDEFGHIJKL","ABCDEFGHIJ","ABCDEFGHIJKLMNOPRS","ABCDEFGHIJK","ABCDEFGHIJKLM","ABCDEFGHIJKL"]
Fmin = [["A->B", "A->C", "B->CD", "G->ABC", "HI->DEFJ", "J->AB", "F->GHI"],["AB->D","B->E","C->AB", "DF->GHK", "DEI->ABC", "BH->JKA", "I->AK"],["AB->EF","CD->FGEH","EO->AHIJK", "L->MN", "N->ABCDEF", "KM->GHIAC", "F->MNO"],["A->A","A->B","B->A","B->B", "CD->ABCDEFGHIJKL", "ME->NOP", "D->M"],["A->BCE","C->EH","DFG->IJKL","L->AB", "B->DEL"],
["A->BCDE","BCD->EFG","CH->I","D->AI", "FA->GHAC"],["A->BCDE","C->AEFGHIJK","K->LMNAOP", "EF->AOKC", "P->AB", "DE->PC"],["AEI->JAC","DE->IFGHA","FAG->A","EFI->DECAB","F->AIJFB"],["BM->JKLADE","MD->FKLJ","G->BCDEF","FI->HIJK", "CE->BMDIF"],["A->B","B->C","C->D","D->E","E->F", "F->G", "G->H", "H->I", "I->J", "J->ABCDEFGHI", "L->J"]]

program = True


while(program):
    mainmenu(R, Fmin)
    canonical_form = []
    odabir = int(input("Unesite broj R sheme ili opcije: "))
    if odabir == (len(R)+3):
        program = False
    elif odabir == (len(R)+1):
        unosNovog(R, Fmin)
    elif odabir == (len(R)+2):
        brisanje(R, Fmin)
        
    else:
        Fmin1 = Fmin[odabir-1]
        R1 = R[odabir-1]

        for att in Fmin1:
            x = att.split('->')
            if(len(x[1])>1):
                for z in x[1]:
                    canonical_form.append(x[0] + "->" + z)
            else:
                canonical_form.append(att)
        
        print("\n")
        print("Fmin:")
        print(Fmin1)
        print("Fmin u kanonskom obliku:")
        print(canonical_form)

        RodF = ""
        for fo in canonical_form:
            x = fo.split('->')
            if(x[0] not in RodF):
                RodF = RodF + x[0]
            if(x[1] not in RodF):
                RodF = RodF + x[1]

        #"set" predefinirana python funkcija izbaci sve nejedinstvene znakove iz stringa, npr "AABBCCDDDDEFG" pretvara u "ABCDEFG"
        RodF = ''.join(sorted(set(RodF)))
        print("R od F je: " + RodF)

        K1 = R1
        K1=K1.replace(RodF,'')

        R1 = R1.replace(K1,'')

        if K1:
            print("\nRazlika atributa je: " + K1)


        L = []
        for FO in Fmin1:
            livi = (FO.split('->'))[0]
            desni = (FO.split('->'))[1]

            
            if livi not in L:
                L.append(livi)
          
        print(L)
        potential_key_candidates = []

        for att in range(1, len(L)+1):
            for subset in itertools.combinations(L, att):
                potential_key_candidates.append(convertTuple(subset))
        #print("Key candidates: " + ', '.join(potential_key_candidates))

        K = []
        tmp = []
        
        for potential_candidate in potential_key_candidates: #moguci kandidati
            temp = potential_candidate
            isUpdated = True
            while(isUpdated):
                isUpdated = False
                for f_dependency in canonical_form: #FO
                    if(f_dependency.split('->')[0] in temp):
                        if f_dependency.split('->')[1] not in temp:
                            #tmp.append(f_dependency.split('->')[1])
                            temp = temp + f_dependency.split('->')[1]
                            isUpdated = True
                            
                            if ''.join(sorted(temp)) == R1:
                                
                                K.append(potential_candidate+K1)
                                    
        print("\nPotencijalni kljucevi su: \n")
        print(K)

        print("\nPrimarni kljuc/kljucevi su: \n")

        for x in K:
            if(len(x) == len(K[0])):
                print(x)
            else:
                break

        
        izlaz = input("\nIzlaz iz programa? (Y/N)")
        if(izlaz == "Y"):
            program = False
