invalid(I) :- size(I,S), S <= 2.
invalid(I) :- size(I,S), S >= 7.
invalid(I) :- C = #sum{V: item(I,V)}, pattern(I), C < 20.

valid(I) :- pattern(I), not invalid(I).

% here should be all individual constraints 
% each constraint should say when a constraint is invalid
1 { selected(I) : valid(I) } 1. 


% % not_subset(J) = I is not a subset of J
not_subset(J) :- selected(I), item(I,Vi), not item(J,Vi), valid(J).
dominated :- selected(I), valid(J), support(I,X), support(J,X), not not_subset(J), I != J.

:- dominated.

#show selected/1.
#show invalid/1.
