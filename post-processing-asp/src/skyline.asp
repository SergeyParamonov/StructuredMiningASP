% here should be all individual constraints 
% each constraint should say when a constraint is invalid

valid(I) :- pattern(I), not invalid(I).

#TODO print itemset size as a predicate here into size(I,S) where I is the itemset id and S is the itemset size

greater_in_size_and_geq_in_frequency(I,J) :- support(I,X), support(J,Y), size(I,Si), size(J, Sj), Si >  Sj, X >= Y. 
geq_in_size_and_greater_in_frequency(I,J) :- support(I,X), support(J,Y), size(I,Si), size(J, Sj), Si >= Sj, X >  Y. 

dominated(I)  :- pattern(I), pattern(J), valid(J), greater_in_size_and_geq_in_frequency(I,J), I != J.
dominated(I)  :- pattern(I), pattern(J), valid(J), geq_in_size_and_greater_in_frequency(I,J), I != J.

condensed(I) :- valid(I), not dominated(I).

#show condensed/1.
