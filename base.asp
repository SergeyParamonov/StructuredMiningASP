threshold(50).

item(V,I) :- db(V,I,_).
transaction(T) :- db(_,_,T).
{ in_itemset(V,I) } :- item(V,I).
in_support(T) :- { conflict_at(T,I) : item(V,I) } 0, transaction(T).
conflict_at(T,I) :- not db(V,I,T), in_itemset(V,I), transaction(T).
:- { in_support(T) } N-1, threshold(N).

#show in_itemset/2.
