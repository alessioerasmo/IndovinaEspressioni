from problema_combinatorio import *
from operazione_su_vettori import *

class IndovinaOperazioni(ProblemaCombinatorio):
    
    def __init__(self, vettore, risultato):
        self.risultato = risultato
        self.vettore = vettore
        self.espressione = []
        self.indicioperazioni = []
        for i in range(len(self.vettore)):
            self.espressione.append(self.vettore[i])
            self.espressione.append(None)
            self.indicioperazioni.append(i*2+1)
        self.espressione.pop()
        self.indicioperazioni.pop()
        self.operazioni = len(self.indicioperazioni)
        self.universo = Universo([somma, sottrazione, divisione, moltiplicazione], self.operazioni)

    def CheckProprietà(self, espressione):
        if (float(CalcolaEspressione(espressione)) == float(self.risultato)):
            print("\ntrovato!,  '" + StringaVettore(espressione) + "'  rispetta il vincolo( =" + str(self.risultato) +" )\n ")
            return True
        else: 
            return False 
 
    def SoluzionePerEnumerazione(self):
        print("\nSoluzione per enumerazione:\nelenco tutte le possibili disposizioni e calcolo il risultato fino a quando non ho trovato quello giusto.")
        tentativi = 0
        while (self.universo.HasNext()):
            test = self.espressione.copy()
            operazioni_tentativo = self.universo.Next()
            for n in range(self.operazioni):
                test[self.indicioperazioni[n]] = operazioni_tentativo[n]
            if (self.CheckProprietà(test)):
                print ("Soluzione trovata al tentativo numero " + str(tentativi)+ "\n\n")
                return test
            tentativi += 1
        print("Non ho trovato nessuna soluzione a questo problema, ho fatto " + str(tentativi) + " tentativi\n\n")
        return False

    def presentati(self):
        print("\n\n'problema 'Indovina Operazioni'\n")
        print("\n   -   vettore operandi:       " + str(self.vettore))
        print("\n   -   espressione da indovinare:      " + str(self.espressione))
        print("\n   -   le operazioni hanno indici:     " + str(self.indicioperazioni))
        print("\n   -   numero operazioni da indovinare:        " + str(self.operazioni))
        print("\n   -   risultato atteso :      " + str(self.risultato))
        print("\n   -   numero di possibili soluzioni(accettabili e non):       " + str(self.universo.Cardinalità()))
        print("\n\n")



