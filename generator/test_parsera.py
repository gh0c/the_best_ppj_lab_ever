#import parser
from parserc import Parser


def main():
    print ('Bok')
    X=open('dat.txt','r')
    pars=Parser(X)
    pars.ucitaj_gramatiku()
    '''
    print(pars.nezavrsni_znakovi)
    
    print(pars.zavrsni_znakovi)
    print(pars.pocetni_nezavrsni_znak)
    print(pars.sinkronizacijski_znakovi)
    
    for x in range (len(pars.produkcije)):
        print (len(pars.produkcije[x].desna_strana))
        print(pars.produkcije[x].lijeva_strana + '->' +
              str(pars.produkcije[x].desna_strana) )
    '''

    
if __name__ == "__main__": main()
