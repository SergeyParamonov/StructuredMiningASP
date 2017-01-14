% here should be all individual constraints 
% each constraint should say when a constraint is invalid
valid(I) :- pattern(I), not invalid(I).

% not_subset(I,J) = I is not a subset of J
not_subset(J) :- selected_item(V), not item(J,V), pattern(J).
% not not_subset(I,J) = I is a subset of a valid itemset J and they have they same support => I is not closed
dominated     :- pattern(J), selected_support(X), support(J,X), valid(J), not not_subset(J), not selected_pattern(J).

condensed :- selected_pattern(I), valid(I), not dominated.

:- not condensed.

#show condensed/0.
