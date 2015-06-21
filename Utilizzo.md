#Configurazione, utilizzo ed integrazione in KMyMoney

# Introduzione #

Lo script fineco2kmymoney è scritto per BASH ed usa solo comandi standard Linux.

Per la prima parte di conversione, per il momento lo script utilizza un piccolo script python di Antonino Sabetta di nome fineco2qif, http://freshmeat.net/projects/fineco2qif

Ho creato, sulla base di fineco2qif, lo script carta2qif; mentre il primo interpreta i movimenti del conto corrente, il secondo i movimenti delle carte di credito.

Lo script di Antonino era ridotto all'osso ma mi ha dato lo stimolo per migliorare il tutto ed integrarlo a KMyMoney.

# Dipendenze #

Per fineco2kymoney basta bash, quindi qualunque distro Linux è ok.

Gli script fineco2qif e carta2qif necessitano di python e del programma xls2csv, contenuto del pacchetto catdoc. Per le distro derivate da Debian (inclusi Ubuntu etc.) è sufficiente eseguire:
```
sudo apt-get install python catdoc
```

Serve ovviamente anche KMyMoney :-)

# Automazione di Beneficiari e Categorie #

Ho cercato di scrivere lo script in modo che si adattasse alle mie esigenze. Una delle cose che mi irrita di più nel "lavorare" un estratto conto è dover modificare manualmente i beneficiari di ogni transazione per renderli leggibili. In KMyMoney una riga così:
```
Pag. Del 26/10/10 Ora 14:00 Presso:Lidl Italia 0511   Via Croix Noire,   26saint Christo   11020     Nfsitanessuna Commissione
```
è veramente odiosa... per non parlare del dover inserire manualmente ogni volta sempre le stesse categorie di spesa. Quante ore buttate!

Ho inserito quindi le funzioni affinché lo script gestisca il lavoro per quelle operazioni che facciamo più e più volte (ad esempio il benzinaio sotto casa, il prelievo di contante dal bancomat, etc.)

# Meccanismo dell'automazione #

L'automazione che ho implementato non è una sofisticata intelligenza artificiale ma è hard-coded nella terminologia che Fineco da anni usa nei propri estratti conto.

Lo script tenta di riconoscere 4 situazioni:

  1. Operazioni frequenti da noi preimpostate col meccanismo search/replace;
  1. Pagamenti PagoBancomat (identificati dalla stringa "Presso:" nell'estratto conto);
  1. Bonifici uscenti (stringa "Ben: " seguita da "Ins:");
  1. Bonifici entranti (stringa "Ord:" seguita da "Ben:");

Lo scenario 1, il più flessibile, viene descritto più sotto.

# Configurazione dello script #

È opportuno rendere avviabili i 3 script; è sufficiente andare nella directory dove sono stati salvati ed eseguire:
```
chmod +x fineco2kmymoney fineco2qif.py carta2qif.py
```

Bisogna, poi, modificare alcuni file per adattarli alle proprie esigenze.

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

# Integrazione in KMyMoney #

## Configurazione ##

L'integrazione è abbastanza semplice.

Lanciare KMyMoney; dal menu _Strumenti_ scegliere _Editor profilo QIF_

Cliccare su _Nuovo_ ed inserire come nome _Fineco XLS_.

Nella sezione _Generale_ mettere come descrizione _Importazione di estratti conto Fineco XLS_.

Nella sezione _Filtro_ impostare la _Posizione del filtro di importazione_ cercando e selezionando lo script _**fineco2kmymoney**_. Mettere quindi _`*`.xls_ come tipo di file.

In _Data_ selezionate _%d/%m/%yyyy_ come _Formato data_.

Cliccate su _OK_.

## Importazione di un estratto conto ##

Dal menu _File_ scegliere _Importa_ e quindi _QIF_.

Prima di tutto scegliere come _Profilo QIF_ il _**Fineco XLS**_ appena creato, poi _Sfoglia_ alla ricerca del file XLS da importare e cliccare su _Importa_.

Talvolta KMyMoney non riesce a comprendere il formato della data; confermare in tal caso _%d/%m/%yyyy_.

Se lo script è stato correttamente configurato _non_ dovrebbe richiedere il conto nel quale importare le operazioni; se lo facesse, selezionare manualmente il conto corrispondente.

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

# Commenti, implementazioni, bug #

Scrivetemi un'email se avete problemi o se volete aiutarmi a migliorare lo script.