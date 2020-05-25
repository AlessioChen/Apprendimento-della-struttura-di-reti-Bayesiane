# Apprendimento-della-struttura-di-reti-Bayesiane
Lo scopo dell'elaborato è quello di apprendere la struttura di una rete Bayesiana a partire da un dataset.
In questo progetto in paritocalre, si apprende la struttura della rete "ASIA".

## Requisiti 
Il linguaggio di programmazione scelto per l'elaborato è Python, utilizzato con l'ambiente di sviluppo PyCharm IDE.

Necessaria l'installazione di alcuni packages nell'ambiente di sviluppo:
* random: implementa generatori di numeri pseudo-casuali per diverse distribuzioni e, nel progetto, viene utilizzato per la generazione del data set.
* itertools: implementa una serie di funzioni per lavorare con data sets iterabili. In questo caso viene utilizzato per la creazione di tutte le possibili configurazioni dei nodi genitori del vertice in questione.
* numpy: implementa funzioni scientifiche ideate per compiere operazioni su vettori e matrici dimensionali, difatti viene utilizzato proprio con questo scopo.
* copy: implementa funzioni utilizzate per la copia di oggetti, dunque viene utilizzato per eseguire la copia del vettore dei nodi.


## File del progetto 

* Node.py : contiene la classe che rappresenta il nodo di una rete Bayesina.
* Bayesnet.py : contiene la classe che rappresenta una rete Bayesiana.
* Input.py: contiene i metodi per prendere in input i dati.
* DFS.py : contiene il metodo di ricerca in profondità per un grafo.
* Learning.py : contine l'algoritmo per l'apprendimento della rete Bayesiana. 
* Main.py: file da eseguire.



