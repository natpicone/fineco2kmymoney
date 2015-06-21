# Configurazione dello script #

È opportuno rendere avviabili i 3 script; è sufficiente andare nella directory dove sono stati salvati ed eseguire:
```
chmod +x fineco2kmymoney fineco2qif.py carta2qif.py
```

Bisogna, poi, modificare alcuni file per adattarli alle proprie esigenze.

Leggete i commenti che ho inserito al sorgente http://code.google.com/p/fineco2kmymoney/source/browse/fineco2kymoney

## File _sostituzioni.grep_ ##

Questo file contiene alcune righe di esempio per renderlo più chiaro.

Il file è strutturato in record su singola linea suddivisi in 3 campi separati da un punto esclamativo.

Esempio:
```
Cerca*!*Sostituisci*!*Categoria:Subcategoria

Android*!*Google Android*!*Computer:Software
```

Lo script cercherà nella descrizione dell'estratto conto la stringa "Android" (case insensitive); qualora la incontrasse, la sostituirà con "Google Android" ed imposterà come categoria di spesa "Software", sottocategoria di "Computer".

Questo rende incredibilmente più leggibile l'estratto conto ed aiuta a preimpostare una buona parte della categorizzazione di spese risparmiando ore di tempo.

## File _fineco2kmymoney_ righe dalla 38 alla 55 ##

Questo è lo script bash vero e proprio. Al momento lo script è in versione alpha quindi bisogna sporcarsi un po' le mani.

Nello script è hard-coded il riconoscimento del tipo di conto (bancario o carta di credito) e su questo viene impostato il "Nome Conto" che verrà passato a KMyMoney in fase di importazione.

In base alla prima riga che lo script trova nel file XLS, estrapola il tipo di conto ed in base a questo imposta la variabile NOMECONTO (che corrisponde al _Nome Conto_ di KMyMoney) e TIPO (che può essere _Bank_ per i conti correnti e _CCard_ per le carte di credito).

Modificare queste linee per adattare lo script alle proprie esigenze.

# Invocazione dello script #

Oltre che essere integrato in KMyMoney lo script può essere invocato anche da linea di comando.

Per specifiche di KMyMoney, lo script deve prendere il file dati dallo standard input e inviare allo standard output un flusso di dati compatibile QIF.

Se si vuole testare manualmente lo script è quindi necessario richiamarlo in questa maniera:
```
cat Movimenti.xls | ./fineco2kmymoney > Movimenti.qif
```