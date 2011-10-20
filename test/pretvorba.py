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
    br2_zagrada = 0
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
            dodaj_epsilon_prijelaz(lijevo_stanje, privremeno_lijevo)
            dodaj_epsilon_prijelaz(privremeno_desno, desno_stanje)
    else:
        prefiksirano = False
        trenutno_stanje = lijevo_stanje
        for i in range(len(regex)):
            if prefiksirano is True:
                prefiksirano = False
                prijelazni_znak = ''
                if regex[i] == 't': prijelazni_znak = '\t'
                elif regex[i] == 'n': prijelazni_znak = '\n'
                elif regex[i] == '_': prijelazni_znak = ' '
                else prijelazni_znak = regex[i]

                sljedece_stanje = novo_stanje()
                dodaj_prijelaz (trenutno_stanje, sljedece_stanje, prijelazni_znak)
                if (i+1) < len(regex) and regex[i+1] == '*':
                    dodaj_epsilon_prijelaz (trenutno_stanje, sljedece_stanje)
                    dodaj_epsilon_prijelaz (sljedece_stanje, trenutno_stanje)
                    i += 1
                trenutno_stanje = sljedece_stanje
            else:
                if regex[i] == '\\':
                    prefiksirano = True
                    continue
                if regex[i] != '(':
                    sljedece_stanje=novo_stanje()
                    if regex[i] == '$':
                        dodaj_epsilon_prijelaz(trenutno_stanje, sljedece_stanje)
                    else:
                        dodaj_prijelaz(trenutno_stanje, sljedece_stanje, regex[i])
                    if (i+1) < len(regex) and regex[i+1] == '*':
                        dodaj_epsilon_prijelaz (trenutno_stanje, sljedece_stanje)
                        dodaj_epsilon_prijelaz (sljedece_stanje, trenutno_stanje)
                        i += 1
                    trenutno_stanje=sljedece_stanje
                else:
                    br2_zagrada += 1
                    for x in range((i+1), len(a)):
                            '''print ('x=%d, %s' % (x,a[x]))'''
                            if a[x] == '(':
                                    br2_zagrada +=1
                            elif a[x] == ')':
                                    br2_zagrada -= 1
                                    if br2_zagrada == 0:
                                        j = x
                                        break
                            else:continue
                    (privremeno_lijevo, privremeno_desno) = pretvori(izbori[(i+1):(j-1)])
                    dodaj_epsilon_prijelaz(trenutno_stanje, privremeno_lijevo)
                    i = j
                    trenutno_stanje = privremeno_desno
                    if (i+1) < len(regex) and regex[i+1] == '*':
                        dodaj_epsilon_prijelaz(privremeno_lijevo, privremeno_desno)
                        dodaj_epsilon_prijelaz(privremeno_desno, privremeno_lijevo)
                        i += 1
            dodaj_epsilon_prijelaz(trenutno_stanje, desno_stanje)
            return (lijevo_stanje, desno_stanje)
        
