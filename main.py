
# Progetto 2 sugli algoritmi di ordinamento e selezione"
# Tutor di riferimento : Pepe' Sciarria
# Simone Festa, matricola 0251679 

import defquick
import copy

if __name__ == "__main__":

    l  = []                                 # Definisco una lista vuota di n elementi.
    n = 50000
    # n = 75000                             # Altre dimensioni analizzate.
    # n = 100000
    # n = 150000
    # n = 200000

    defquick.randomList(l, n)               # Assegno in modo random gli elementi alla lista creata.

    l1 = copy.copy(l)                       # Creo delle copie della lista per gli altri algoritmi.
    l2 = copy.copy(l)
    l3 = copy.copy(l)

    defquick.quickSort(l,  0)               # QuickSort classico non det.
    defquick.quickSort(l1, 1)               # QuickSort con Select Deterministica
    defquick.quickSort(l2, 2)               # QuickSort con Select Randomizzata
    #print(l3)                              # Posso anche verificare l'effettivo funzionamento dell'algoritmo.
    defquick.quickSort(l3, 3)               # QuickSort con SampleMedianSelect
    #print(l3)
