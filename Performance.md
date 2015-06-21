# Performance #

Inizialmente lo script andava alla "vertiginosa" velocità di un'operazione al secondo; per analizzarmi 5 anni di estratto conto ci metteva 34 minuti; questo era anche dovuto al fatto che avevo configurato un centinaio di sostituzioni col file _sostituzioni.grep_. Volevo morire.

Ho fatto parecchie "ottimizzazioni" ed ora su un quad-core lo script macina 24 operazioni al secondo con 111 righe di sostituzioni.

Nonostante sia orgoglioso di un'ottimizzazione 24:1, per un quad-core è ancora una lumaca;  non capita tutti i giorni, però, di dover importare un estratto conto di 5 anni composto da più di 2.000 operazioni bancarie; per questo lavoro lo script impiega meno di un minuto e mezzo. Accettabile.
```
$ time cat Movimenti.xls | ./fineco2kymoney > /dev/null

real	1m28.596s
user	0m26.170s
sys	0m9.450s
```