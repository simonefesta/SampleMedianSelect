from time import time
from selection import partition
import random

def randomList (l, n):

   # Creo lista random
   l.clear ()
   for i in range (0, n):
        l.append (random.randint (0, n))

def quickSort(l,type):

    # Chiamo la ricorsione, misuro il tempo e lo stampo dopo aver terminato.
    start = time()
    recursiveQuickSort(l, 0, len(l) - 1,type)
    tempotot = time() - start
    if type == 0:
        name = "- QuickSort random"
    elif type == 1:
        name = "- QuickSort con select deterministico"
    elif type == 2:
        name = "- QuickSort con select randomizzata"
    elif type == 3:
        name = "- QuickSort con SampleMedianSelect"

    print(" ")
    print(name, ", tempo richiesto : ",tempotot, "secondi.")



def recursiveQuickSort(l, left, right, type):

    if left >= right:
        return
    mid = partition(l, left, right, type)
    recursiveQuickSort(l, left, mid - 1, type)
    recursiveQuickSort(l, mid + 1, right, type)




