% what is valid is defined via local constraints such as invalid(I) :- size(I), I < 5.

invalid(I) :- size(I,S), S <= 2.
invalid(I) :- size(I,S), S >= 7.
invalid(I) :- C = #sum{V: item(I,_,V)}, pattern(I), C < 20.

valid(I) :- pattern(I), not invalid(I).

% for every pattern guess whether it is maximal (selected)
1 { selected(I) : valid(I)} 1.

% if V appears in I, derive in(V,I)
in(V,I) :- item(I,P,V).

% I is not a subset of J if I has V that J does not have
not_subset_of(J) :- selected(I), valid(J), I != J, item(I,P,V), not in(V,J).

% if for a subseq <V,W> in I there is V followed by W in J then deduce domcand(V,J)
domcand(V,J) :- selected(I), item(I,P,V), item(I,P+1,W), valid(J), item(J,Q,V), item(J,Q1,W), Q1>Q, I != J.

% if domcand(V,J) does not hold for some V in I and a pattern J then derive not_dominated_by(J)
not_dominated_by(J) :- selected(I), item(I,P,V), item(I,P+1,W), valid(J), I != J, not domcand(V,J).

% if neither not_dominated_by(J) nor not_subset_of(J) are derived for some J, then I is dominated
dominated :- selected(I), valid(J), I != J, not not_subset_of(J), not not_dominated_by(J), support(I,X), support(J,X). 

% forbid models with dominated selected patterns
:- dominated.

#show selected/1.
%#show invalid/1.

