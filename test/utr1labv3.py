class Stanje:
    def __init__(self, ime):
        self.ime = ime
        self.prijelazi = dict()

    def dodajPrijelaz(self, znak, stanja):
        try:
            lista = self.prijelazi[znak]
        except KeyError:
            lista = list()
            self.prijelazi[znak] = lista
        lista.extend(stanja)

class Automat:
    def __init__(self):
        self.skupStanja = set()
        self.skupUlaza = set()
        self.prihvatljiva = set()
        self.pocetno = ""

        self.stanja = dict()

    def dodajPrijelaz(self, prijelaz):
        elementi = prijelaz.split('->')
        lijevo = elementi[0].split(',')
        desno = elementi[1].split(',')
        
        try:
            s = self.stanja[lijevo[0]]
        except KeyError:
            s = Stanje(lijevo[0])
            self.stanja[lijevo[0]] = s

        s.dodajPrijelaz(lijevo[1], desno)

    def stvoriStanja(self):
        for i in self.skupStanja:
            s = Stanje(i)
            self.stanja[i] = s

    def epsilon(self, stanje, eokru):
        try:
            eps = stanje.prijelazi['$']
        except KeyError:
            return eokru

        for e in eps:
            if e not in eokru:
                eokru.append(e)
                self.epsilon(self.stanja[e], eokru)

        return eokru

    def simulacija(self, ulaz):
        print '\n***** SIMULACIJA *****'
        print 'Ulazni niz: ', ulaz
        trenutno=set()
        trenutno.add(self.pocetno)
        for i in self.epsilon(self.stanja[self.pocetno], []):
            trenutno.add(i)

        for z in ulaz:
            print 'Trenutni skup stanja: ',trenutno
            print 'dolazi ulazni znak:', z

            novoTrenutno = list()
            while len(trenutno) > 0:
                s = self.stanja[trenutno.pop()]
                try:
                    nova = s.prijelazi[z]
                    novoTrenutno.extend(nova)

                    print s.ime + '->', nova
                    
                except KeyError:
                    print s.ime + ' nema prijelaz.'
                    continue

                for nov in nova:
                    eokruzenje = self.epsilon(self.stanja[nov], [])
                    novoTrenutno.extend(eokruzenje)

            trenutno = set(novoTrenutno)

        print 'Na kraju je u skupu stanja: ', trenutno
        prihv = 0
        for i in trenutno:
            if i in self.prihvatljiva:
                prihv = 1
                break

        if prihv == 1:
            print 'Prihvaca se ulazni niz'
        else:
            print 'Ne prihvaca se ulazni niz'
            
def main():
    at = Automat()
    fob=open('definicija.txt')
    at.skupStanja = fob.readline().split("\n")[0].split(",")
    at.skupUlaza = fob.readline().split("\n")[0].split(",")
    at.prihvatljiva = fob.readline().split("\n")[0].split(",")
    at.pocetno = fob.readline().split("\n")[0]
    at.stvoriStanja()
    prijelazi = fob.readlines()
    for p in prijelazi:
        at.dodajPrijelaz(p.split("\n")[0])
    fob.close()
    fob=open('ulaz.txt')
    while True:
        red = fob.readline().split("\n")[0]
        if red == '':
            break
        at.simulacija(red)
    fob.close()
    
    x=raw_input('Stisni <enter> za kraj simulacije')
if __name__=="__main__":    main()
