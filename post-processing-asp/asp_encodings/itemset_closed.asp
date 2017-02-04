% here should be all individual constraints 
% each constraint should say when a constraint is invalid
1 { selected(I) : pattern(I) } 1. 

% % not_subset(J) = I is not a subset of J
not_subset(J) :- selected(I), item(I,Vi), not item(J,Vi), pattern(J).
dominated :- selected(I), pattern(J), support(I,X), support(J,X), not not_subset(J), I != J.

:- dominated.

#show selected/1.
