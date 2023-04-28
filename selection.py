from math import ceil
import random

""" 
    SAMPLE MEDIAN SELECT
"""
def SampleMedianSelect(l, k,minLen):
    if k <= 0 or k > len(l):
        return None
    return RecursiveSampleMedianSelect(l, 0, len(l) - 1, k,minLen)


def RecursiveSampleMedianSelect(l, left, right, k, minLen):

    # Implemento dei controlli iniziali
    if left == right:
       return l[left]

    if right - left < minLen:
        med = trivialSelect(l[left: right + 1], k - left)
        return med

    # Estraggo m valori random, aggiungendoli a V.
    # Per estrarre m elementi, estraggo un elemento per ciascuno degli m gruppi.
    m = 5                                                                # Il numero di gruppi, i test sono stati anche effettuati con m = 1 ed m = 7
    V = []
    numElem = right - left + 1
    numGroups = m
    numElemforGroups =  int(numElem/numGroups)
    for i in range(0, numGroups):
        if i == numGroups - 1 :
            valIndice = random.randint(i * numElemforGroups, right-left)
        else:
            valIndice= random.randint(i*numElemforGroups,(i+1)*numElemforGroups)

        V.append(l[valIndice+left])

    # Trovo il valore vperno, richiamo prima il SampleMedian e successivamente partitionDet

    vperno = SampleMedianSelect(V, ceil(m/ 2),minLen)


    perno = partitionDet(l, left, right, vperno)


    posperno = perno + 1

    # Controlli su posperno.

    if posperno == k:
        return l[perno]
    if posperno > k:
        return RecursiveSampleMedianSelect(l, left, perno - 1, k,minLen)
    else:
        return RecursiveSampleMedianSelect(l, perno + 1, right, k,minLen)

"FINE SAMPLE"


# Nelle righe seguenti sono presenti i select determistici e randomizzati.

def trivialSelect(l, k):
    length = len(l)
    if k <= 0 or k > length:
        return None

    for i in range(0, k):
        minimum = i
        for j in range(i + 1, length):
            if l[j] < l[minimum]:
                minimum = j
        l[minimum], l[i] = l[i], l[minimum]

    return l[k - 1]

""" 
   SELECT RANDOMIZZATO
"""

def quickSelectRand(l, k):
    if k <= 0 or k > len(l):
        return None
    return recursiveQuickSelectRand(l, 0, len(l) - 1, k)


def recursiveQuickSelectRand(l, left, right, k):

    if left > right:
        return
    if left == right and k - 1 == left:
        return l[k - 1]
    mid = partition(l, left, right, 0)

    if k - 1 == mid:
        return l[mid]
    if k - 1 < mid:
        return recursiveQuickSelectRand(l, left, mid - 1, k)
    else:
        return recursiveQuickSelectRand(l, mid + 1, right, k)

""" 
    SELECT DETERMINISTICO
"""


def quickSelectDet(l, k, minLen, whoami="QuickSelectDet"):
    if k <= 0 or k > len(l):
        return None
    return recursiveQuickSelectDet(l, 0, len(l) - 1, k, minLen, whoami)


def recursiveQuickSelectDet(l, left, right, k, minLen, whoami):

    if left == right:
        return l[left]

    if len(l) < minLen:
        med = trivialSelect(l[left: right + 1], k - left)
        return med

    numElem = right - left + 1
    numGroups = int(ceil(numElem / 5.0))
    median = []
    for i in range(0, numGroups):
        dimGroup = 5 if (i < numGroups - 1 or numElem % 5 == 0) \
            else (numElem - (numGroups - 1) * 5)
        a = left + i * 5
        b = left + i * 5 + dimGroup - 1

        m = trivialSelect(l[a:b + 1], int(ceil(dimGroup / 2.0)))
        median.append(m)


    vperno = quickSelectDet(median, ceil(len(median) / 2), minLen)

    perno = partitionDet(l, left, right,vperno)

    posperno = perno + 1
    if posperno == k:
        return l[perno]
    if posperno > k:
        return recursiveQuickSelectDet(l, left, perno - 1, k, minLen, whoami)
    else:
        return recursiveQuickSelectDet(l, perno + 1, right, k, minLen, whoami)


def partitionDet(l, left, right, pivot):
    inf = left
    sup = right

    while True:
        while inf <= right and l[inf] <= pivot:
            if l[inf] == pivot and l[left] != pivot:
                l[left], l[inf] = l[inf], l[left]
            else:
                inf += 1

        while sup >= 0 and l[sup] > pivot:
            sup -= 1

        if inf < sup:
            l[inf], l[sup] = l[sup], l[inf]
        else:
            break

    l[left], l[sup] = l[sup], l[left]
    return sup

# Qui troviamo la particion, che implementa le varie select al seconda del parametro type scelto.

def partition(l, left, right, type):
    inf = left
    sup = right + 1
    median = ceil ((right-left)/2)

    if type == 0:
        midIndex = random.randint(left, right)
        midValue = l[midIndex]
        l[midIndex], l[left] = l[left], l[midIndex]
    if type == 1:
        midValue = quickSelectDet(l[left:right+1],median+1,10)
    if type == 2:
        midValue = quickSelectRand(l[left:right+1],median+1)

    if type == 3:
        midValue = SampleMedianSelect(l[left:right+1],median+1,10)

    midIndex=left

    while True:
        inf += 1
        while inf <= right and l[inf] <= midValue:
            if l[inf] == midValue and not l[left] == midValue:
                l[inf], l[left] = l[left], l[inf]
            else:
                 inf += 1

        sup -= 1

        while l[sup] >= midValue:
            if l[sup] == midValue and not l[left] == midValue:
                l[sup], l[left] = l[left], l[sup]
            elif l[sup] > midValue:
                 sup -= 1
            else:
                break

        if inf < sup:
            l[inf], l[sup] = l[sup], l[inf]
        else:
            break

    l[midIndex], l[sup] = l[sup], l[midIndex]

    return sup
