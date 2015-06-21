# Introduzione #

Lo script fineco2kmymoney è scritto per BASH ed usa solo comandi standard Linux.

Per la prima parte di conversione, per il momento lo script utilizza un piccolo script python di Antonino Sabetta di nome fineco2qif, http://freshmeat.net/projects/fineco2qif

Ho creato, sulla base di fineco2qif, lo script carta2qif; mentre il primo interpreta i movimenti del conto corrente, il secondo i movimenti delle carte di credito.

Lo script di Antonino era ridotto all'osso ma mi ha dato lo stimolo per migliorare il tutto ed integrarlo a KMyMoney.

# Performance #

Sulla mia macchina (AMD Phenom 965 QuadCore con Ubuntu 64bit e disco SSD) ed un file di sostituzioni composto da 260 righe lo script analizza 533 operazioni bancarie in 45 secondi con una media di circa 12 operazioni al secondo; senza righe di sostituzione esegue 19 operazioni al secondo.

# ATTENZIONE #

Nei sorgenti il file fineco2kmymoney è stato erroneamente uploadato come fineco2kymoney.

Lo script funziona, l'errore è solo nel nome del file, che è sufficiente rinominare.

Alla prossima release correggerò il problema.