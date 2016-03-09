threshold(5).
col(1..10).
val(x). val(o).

item(V,I) :- db(V,I,_).
transaction(T) :- db(_,_,T).
{ in_itemset(V,I) } :- item(V,I).
bad_transation(T) :- conflict_at(T,_).
in_support(T) :- not bad_transation(T), transaction(T).
conflict_at(T,I) :- not db(V,I,T), in_itemset(V,I), transaction(T).
:- { in_support(T) } N-1, threshold(N).

support(N) :- N = #count{T:in_support(T)}.

% closed constraints
in(x,1) | in(o,1) | in(x,2) | in(o,2) | in(x,3) | in(o,3) | in(x,4) | in(o,4) | in(x,5) | in(o,5) | in(x,6) | in(o,6) | in(x,7) | in(o,7) | in(x,8) | in(o,8) | in(x,9) | in(o,9) | in(x,10) | in(o,10). 
sat :- not db(V,I,T), in(V,I), in_support(T).
sat :- in(V,I), in_itemset(V,I).

%saturation
in(V,I)  :- sat, col(I), val(V).

:- not sat. % if sat, then the itemset is ok, it is closed

#show in_itemset/2.
#show sat/0.
#show support/1.
