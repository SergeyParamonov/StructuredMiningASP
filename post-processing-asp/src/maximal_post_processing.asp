% here should be all individual constraints 
% each constraint should say when a constraint is invalid
valid(I) :- pattern(I), not invalid(I).

% not_subset(I,J) = I is not a subset of J
not_subset(I,J) :- item(I,Vi), not item(J,Vi), pattern(J), I != J. % I != J is not necessary here, but I guess it should propagate better
% not not_subset(I,J) = I is a subset of a valid itemset J and they have they same support => I is not closed
dominated(I)    :- pattern(I), pattern(J), valid(J), not not_subset(I,J), I != J.

condensed(I) :- valid(I), not dominated(I).

#show condensed/1.
