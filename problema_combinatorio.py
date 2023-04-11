import math
import numpy as np

class Universo:

    def __init__(self, InsiemeBase, NumeroElementi ):
        # dominio degli elementi che compongono l'universo
        self.base = InsiemeBase
        # numero di elementi che ha un'istanza dell'universo
        self.elementi = NumeroElementi
        # imposta l'iteratore
        self.Reset()

    def InsiemeBase(self):
        return self.base
    
    def NumeroElementi(self):
        return self.elementi
    
    def Cardinalità(self):
        return math.pow(len(self.base), self.elementi)
    
    def HasNext(self):
        for i in range(self.elementi):
            if (self.vettore[i] < len(self.base)- 1):
                return True
        return False 
    
    def Next(self):
        if (self.SommaVettore(self.elementi - 1)):
            elemento = []
            for i in range(self.elementi):
                elemento.append(self.base[self.vettore[i]])
            return elemento
        else:
            return None
    
    def Reset(self):
        self.vettore = []
        for i in range(self.elementi):
            self.vettore.append(0)
        self.vettore[self.elementi - 1] = -1
        self.next = True

    def SommaVettore(self, i):
        if (self.vettore[i] < len(self.base)-1):
            self.vettore[i] = self.vettore[i]+1
        else:
            self.vettore[i] = 0
            if (( i-1) == -1):
                self.vettore[self.elementi - 1] = -1 
                return False
            else : 
                self.SommaVettore(i-1)
        return True

class ProblemaCombinatorio:

    def __init(*args):
        pass

    def CheckProprietà():
        pass

    def Soluzione():
        pass

#   universo = Universo(["somma","sottrazione", "divisione", "moltiplicazione"], 4)

#   list = []
#   while(universo.HasNext()):
#        list.append(universo.Next())

#   print(len(list))
#   print(universo.Cardinalità())

#   universo.Reset()
 
#   while(universo.HasNext()):
#       print(universo.Next())
