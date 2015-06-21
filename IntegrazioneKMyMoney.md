# Integrazione in KMyMoney #

## Configurazione ##

L'integrazione è abbastanza semplice.

Lanciare KMyMoney; dal menu _Strumenti_ scegliere _Editor profilo QIF_

## Opzione 1 ##

Cliccare su _Nuovo_ ed inserire come nome _Fineco XLS_.

Nella sezione _Generale_ mettere come descrizione _Importazione di estratti conto Fineco XLS_.

Nella sezione _Filtro_ impostare la _Posizione del filtro di importazione_ cercando e selezionando lo script _**fineco2kmymoney**_. Mettere quindi _`*`.xls_ come tipo di file.

In _Data_ selezionate _%d/%m/%yyyy_ come _Formato data_.

Cliccate su _OK_.

## Opzione 2 ##

Nella sezione _Filtro_ impostare la _Posizione del filtro di importazione_ cercando e selezionando lo script _**fineco2kmymoney**_. Mettere quindi _"`*`.qif `*`.xls"_ (senza virgolette, notate lo spazio) come tipo di file.

In _Data_ selezionate _%d/%m/%yyyy_ come _Formato data_.

Cliccate su _OK_.

## Importazione di un estratto conto ##

Dal menu _File_ scegliere _Importa_ e quindi _QIF_.

Prima di tutto scegliere come _Profilo QIF_ il _**Fineco XLS**_ appena creato, poi _Sfoglia_ alla ricerca del file XLS da importare e cliccare su _Importa_.

Talvolta KMyMoney non riesce a comprendere il formato della data; confermare in tal caso _%d/%m/%yyyy_.

Se lo script è stato correttamente configurato _non_ dovrebbe richiedere il conto nel quale importare le operazioni; se lo facesse, selezionare manualmente il conto corrispondente.