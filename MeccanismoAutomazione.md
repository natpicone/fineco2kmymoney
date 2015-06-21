# Meccanismo dell'automazione #

L'automazione che ho implementato non è una sofisticata intelligenza artificiale ma è hard-coded nella terminologia che Fineco da anni usa nei propri estratti conto.

Lo script tenta di riconoscere 4 situazioni:

  1. Operazioni frequenti da noi preimpostate col meccanismo search/replace;
  1. Pagamenti PagoBancomat (identificati dalla stringa "Presso:" nell'estratto conto);
  1. Bonifici uscenti (stringa "Ben: " seguita da "Ins:");
  1. Bonifici entranti (stringa "Ord:" seguita da "Ben:");

Lo scenario 1, il più flessibile, viene descritto più sotto.