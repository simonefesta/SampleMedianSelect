# SampleMedianSelect
Progetto in itinere di "Ingegneria degli Algoritmi", a.a. 2018/2019

La realizzazione dell’algoritmo SampleMedianSelect è basata sulla select deterministica. In 
particolare, per la creazione del sottoinsieme V di m elementi, viene partizionata la lista di elementi in 
m gruppi, prelevando in modo random un indice da ciascun gruppo ed aggiungendo l’elemento di 
indice “ i “ presente nella lista nel sottoinsieme V.
Ottenuto un sottoinsieme V di m elementi, procedo con il calcolo del mediano, utilizzandolo come 
pivot. La partizione verrà eseguita con riferimento a tale pivot.
Le restanti linee di codice sono fedeli alla select deterministica, come l’implementazione del 
TrivialSelect per liste di piccole dimensioni o le partizioni rispetto ad un determinato perno.
