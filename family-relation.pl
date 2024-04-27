%Facts
male(umer).
male(ahmed).
male(abdulmajeed).
male(rehan).
male(hanif).
male(saim).
male(khalid).
male(abdulhameed).
female(qusar).
female(alia).
female(ma-g).
female(dadi).


parent(abdulmajeed,ahmed).
parent(abdulmajeed,umer).
parent(abdulmajeed,qusar).
parent(ma-g,ahmed).
parent(ma-g,umer).
parent(hanif,rehan).
parent(khalid,saim).
parent(abdulmajeed,alia).
parent(abdulhameed,abdulmajeed).
parent(dadi,abdulmajeed).


%Rules
mother(X,Y):- parent(X,Y), female(X).
father(X,Y):- parent(X,Y), male(X).
brother(X,Y):- male(X), parent(Z,X), parent(Z,Y), X \== Y.
sister(X,Y):- female(X), parent(Z,X), parent(Z,Y), X \== Y.
siblings(X,Y):- parent(Z,X),parent(Z,Y), X\==Y.
husband(X,Y):- male(X),female(Y),parent(X,Z),parent(Y,Z).
wife(Y,X):- male(X),female(Y),parent(X,Z),parent(Y,Z).
grandfather(X,Y):-  male(X),parent(X,Z),parent(Z,Y).
grandmother(X,Y):-  female(X),parent(X,Z),parent(Z,Y).
grandparents(X,Y):- parent(X,Z),parent(Z,Y).
grandchild(X,Y):- parent(Z,X),parent(Y,Z).

ancestor(X,Y):- parent(X,Y).
ancestor(X,Y):- parent(X,Z), ancestor(Z,Y).
