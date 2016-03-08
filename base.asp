threshold(100).

item(V,I) :- db(V,I,_).
transaction(T) :- db(_,_,T).
{ in_itemset(V,I) } :- item(V,I).
bad_transation(T) :- conflict_at(T,_).
in_support(T) :- not bad_transation(T), transaction(T).
conflict_at(T,I) :- not db(V,I,T), in_itemset(V,I), transaction(T).
:- { in_support(T) } N-1, threshold(N).

in(V,I) | out(V,I) :- item(V,I), not in_itemset(V,I).
in_conflict(T) :- not db(V,I,T), in(V,I), transaction(T).
sat :- in_support(T), in_conflict(T).

%saturation
in(V,I)  :- sat, item(V,I).
out(V,I) :- sat, item(V,I).

#show in_itemset/2.
