% what is valid is defined via local constraints such as invalid(I) :- size(I), I < 5.
valid(I) :- pattern(I), not invalid(I).

% for every pattern guess whether it is maximal (selected)
1 { selected(I) : valid(I)} 1.

% (1) sup(I) <= sup(J) and size(I) < size(J)
geq_sup_g_size(J) :- selected(I), valid(J), I != J, support(I,X), support(J,Y), X<=Y, size(I,X1), size(J,Y1), X1<Y1.

% (2) sup(I) < sup(J) and size(I) <= size(J)
g_sup_geq_size(J) :- selected(I), valid(J), I != J, support(I,X), support(J,Y), X<Y, size(I,X1), size(J,Y1), X1<=Y1.

% if neither (1) nor (2) holds for J, I is not dom. by J
not_dominated_by(J) :- selected(I), I != J, valid(J), not geq_sup_g_size(J), not g_sup_geq_size(J).

% otherwise it is
dominated :- selected(I), valid(J), I != J, not not_dominated_by(J).

:-dominated.

#show selected/1.
