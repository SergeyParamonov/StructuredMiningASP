%to be tested on "fake dataset", disjunctive atoms are hardcoded and they need to be changed for other datasets

max_cost(8).
threshold(4).
col(1..10).
val(x). val(o). val(b).

item(V,I) :- db(V,I,_).
transaction(T) :- db(_,_,T).
{ in_itemset(V,I) } :- item(V,I).
used_colums(I) :- in_itemset(V,I).
:- N+1 { used_colums(I) }, max_cost(N). % cost constraint

bad_transation(T) :- conflict_at(T,_).
in_support(T) :- not bad_transation(T), transaction(T).
conflict_at(T,I) :- not db(V,I,T), in_itemset(V,I), transaction(T).
:- { in_support(T) } N-1, threshold(N).

support(N) :- N = #count{T:in_support(T)}.

% closed constraints
in(x,1) | in(o,1) | in(x,2) | in(o,2) | in(x,3) | in(o,3) | in(x,4) | in(o,4) | in(x,5) | in(o,5) | in(x,6) | in(o,6) | in(x,7) | in(o,7) | in(x,8) | in(o,8) | in(x,9) | in(o,9) | in(x,10) | in(o,10) | in(b,1) | in(b,2) | in(b,3) | in(b,4) | in(b,5) | in(b,6) | in(b,7) | in(b,8) | in(b,9) | in(b,10).
sat :- not db(V,I,T), in(V,I), in_support(T).
sat :- in(V,I), in_itemset(V,I).
sat :- N { used_colums(I) }, max_cost(N). % cost constraint added for saturation

%saturation
in(V,I)  :- sat, col(I), val(V).


:- not sat. % if sat, then the itemset is ok, it is closed

#show in_itemset/2.
#show sat/0.
#show support/1.
