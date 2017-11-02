% what is valid is defined via local constraints such as invalid(I) :- size(I), I < 5.
valid(I) :- pattern(I), not invalid(I).

% for every pattern guess whether it is maximal (selected)
1 { selected(I) : valid(I)} 1.

% if V appears in I, derive in(V,I)
in(V,I) :- item(I,P,V).

% I is not a superset of J if J has V that I does not have
not_superset(J) :- selected(I), in(V,J), not in(V,I), I != J.

% superpattern check
domcand(V,J) :- selected(I), item(J,P,V), item(J,P+1,W), item(I,Q,V), item(I,Q1,W),Q1>Q, I != J.
not_dominated_by(J) :- selected(I), valid(J), I != J, item(J,P,V), item(J,P+1,W), not domcand(V,J). 

% if neither not_dominated_by(J) nor not_superset_of(J) are derived for some J, then I is dominated
dominated :- selected(I), valid(J), I != J, not not_superset_of(J), not not_dominated_by(J), support(I,X), support(J,X). 

% forbid models with dominated selected patterns
:- dominated.

#show selected/1.
