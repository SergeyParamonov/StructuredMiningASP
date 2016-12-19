item(I) :- db(_,I).
transaction(T) :- db(T,_).
{ in_itemset(I) } :- item(I), N { in_support(T) : db(T,I) }, threshold(N).
in_support(T) :- { conflict_at(T,I) : item(I) } 0, transaction(T).
conflict_at(T,I) :- not db(T,I), in_itemset(I), transaction(T).

#show in_itemset/1.
