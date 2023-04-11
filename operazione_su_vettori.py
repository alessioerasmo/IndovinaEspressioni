def somma(a,b):
    return a + b
somma.__str__ = lambda : "+"

def sottrazione(a,b):
    return a - b

def moltiplicazione(a,b):
    return a * b

def divisione(a, b):
    return a/b

def exec_operazione(vettore, indiceoperazione):
    i = indiceoperazione
    # eseguo la funzione sul vettore
    vettore[i-1] = vettore[i](vettore[i-1], vettore[i+1] )
    # faccio lo shift di due per ottenere il vettore risultante
    j = i
    while (j < len(vettore)-2):
        vettore[j]= vettore[j+2]
        j = j + 1
    vettore.pop()
    vettore.pop()
    return vettore

def valuta_ordine(vettore):
    # ritorna un vettore contenente gli indici degli operatori posizionati secondo l'ordine di esecuzione
    i = 1
    alta_priorità = []
    bassa_priorità = []
    while (i < len(vettore)-1):
        if ((vettore[i] == moltiplicazione) | (vettore[i] == divisione)):
            alta_priorità.append(i)
        else: 
            if ((vettore[i]== somma) | (vettore[i] == sottrazione)):
                bassa_priorità.append(i)
            else:
                return 0
        i = i+2
    for i in bassa_priorità:
        alta_priorità.append(i)
    return alta_priorità


def CalcolaEspressione(espressione):
    vettore = espressione.copy()
    # trovo l'ordine di esecuzione delle operazioni
    valutazione = valuta_ordine(vettore)
    # creo lo stack delle operazioni da fare, e faccio in modo che sul top ci sia la prossima operazione
    stack = valutazione[::-1]

    while(len(stack) > 0):
        # indice prossima operazione da eseguire 
        indice = stack.pop()
        # eseguo l'operazione sul vettore
        vettore = exec_operazione(vettore, indice)
        # ora devo aggiornare gli indici
        i = 0
        while (i < len(stack)):
            if (stack[i]>indice):
                stack[i] = stack[i]-2
            i+=1
    return vettore[0]

def StringaVettore(espressione):
    StringaVettore = ""
    for i in espressione:
        if (i == somma):
            StringaVettore = StringaVettore + " + "
        elif i == sottrazione:
            StringaVettore = StringaVettore +" - "
        elif i == moltiplicazione:
            StringaVettore = StringaVettore+  " * "
        elif i == divisione:
            StringaVettore = StringaVettore+  "/"
        else:
            StringaVettore =StringaVettore + str(i)
    return StringaVettore

# var = [1, somma, 2, somma, 3, sottrazione, 4,somma,3, sottrazione, 4, moltiplicazione, 3, sottrazione, 4,divisione, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4,somma, 2, somma, 3, sottrazione, 4]
# print(CalcolaEspressione(var))
