def novo_stanje( self ):
    self.br_stanja += 1
    return self.br_stanja - 1

def je_operator( regex, i ):
    br = 0
    while(i-1 >= 0 and regex[i-1] == '\\'):
        br += 1
        i -= 1
    return br%2 == 0

def pretvori( regex ):
 
    izbori = list()
    x = 0
    br_zagrada = 0
    br_op_izbora = 0
    
    for i in range(len(regex)):
        if regex[i] == '(' and je_operator(regex, i):
            br_zagrada += 1
        elif regex[i] == ')' and je_operator (regex, i):
            br_zagrada -= 1
        elif br_zagrada == 0 and regex[i] == '|' and je_operator(regex, i):
            
            izbori.append(regex[x:i])
            print (len(regex[x:i]))
            print (len(izbori[br_op_izbora]))
            print ('\n', izbori, len(izbori))
            br_op_izbora +=1
            x = i + 1   

    if br_op_izbora > 0:
        izbori.append(regex[x:])
        
    lijevo_stanje = novo_stanje()
    desno_stanje = novo_stanje()
    if br_op_izbora > 0:
        for i in range(len(izbori)):
            (privremeno_lijevo, privremeno_desno) = pretvori(izbori[i])
            dodaj_epsilon_prijelaz(lijevo_sranje, privremeno_lijevo)
            dodaj_epsilon_prijelaz(privremeno_desno, desno_stanje)
    else:
        prefiksirano = False
        trenutno_stanje = lijevo_stanje
        for i in range(len(izraz)):
            if prefiksirano is True:
                    
            
        
        
