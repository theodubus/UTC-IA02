% cas de base
nBienPlace([], [], 0).

% cas recursif positif
nBienPlace([T1|R1], [T1|R2], BP) :-
    nBienPlace(R1, R2, BP2),
    BP is BP2 + 1.

% cas recursif negatif
nBienPlace([T1|R1], [T2|R2], BP) :-
    dif(T1, T2),
    nBienPlace(R1, R2, BP).

% cas de base
longueur([], 0).

% cas recursif
longueur([_|R], N):-
    longueur(R, N2),
    N is N2 + 1.

% gagne
gagne(Code1, Code2):-
    nBienPlace(Code1, Code2, BP),
    longueur(Code1, BP),
    longueur(Code2, BP).

% element
%element(E, L):-
%    member(E, L).

% cas positif
element(E, [E|_]).

% cas recursif
element(E, [T|R]):-
    dif(T, E),
    element(E, R).

% cas de base
enleve(_, [], []).

% Debut de liste = premier element de L1
enleve(E, [E|R], R).

% Debut de liste != premier element de L1 (E2), Appel sur R
% et concaténation du resultat de l'appel (Ltemp) avec E2.
enleve(E1, [E2|R], [E2|Ltemp]):-
    dif(E1, E2),
    enleve(E1, R, Ltemp).

% cas de base
enleveBP([], [], [], []).

% cas premier element identique
enleveBP([E1|R1], [E1|R2], Code1Bis, Code2Bis):-
    enleveBP(R1, R2, Code1Bis, Code2Bis).

% cas premier element different
enleveBP([E1|R1], [E2|R2], [E1|R1Bis], [E2|R2Bis]):-
    dif(E1,E2),
    enleveBP(R1, R2, R1Bis, R2Bis).


% Enlever les BP
nMalPlaces(Code1, Code2, MP):-
    enleveBP(Code1, Code2, Code1Bis, Code2Bis),
    nMalPlacesAux(Code1Bis, Code2Bis, MP).

% cas de base
nMalPlacesAux([], _, 0).

% 1er elt de Code1 dans Code2
nMalPlacesAux([T|R], Code2, MP):-
    element(T, Code2),
    enleve(T, Code2, Code2Bis),
    nMalPlacesAux(R, Code2Bis, MPtemp),
    MP is MPtemp + 1.

% 1er elt de Code1 pas dans Code2
nMalPlacesAux([T|R], Code2, MP):-
    \+ element(T, Code2),
    nMalPlacesAux(R, Code2, MP).

% cas de base
codeur(_, 0, []).

% cas général
codeur(M, N, [T|Codetemp]):-
    N > 0,
    Nbis is N-1,
    MMax is M+1,
    codeur(M, Nbis, Codetemp),
    random(1, MMax, T).

% fonctions de service
demanderCode(Code):-
    write('Donnez un code : '),
    read(Code),
    nl.

afficherRestant(N):-
    write('Il vous reste '),
    write(N),
    write(' coups.'),
    nl.

afficherBpNp(BP, MP):-
    write('BP : '),
    write(BP),
    write(' MP : '),
    write(MP),
    nl.

% cas code faux
verif(Code, BonCode, Nrestant):-
    \+ gagne(Code, BonCode),
    write('Code faux !'),
    Nrestantbis is Nrestant - 1,
    jeu(BonCode, Nrestantbis).

% cas code vrai
verif(Code, BonCode, _):-
    gagne(Code, BonCode),
    write('Vous avez gagné !'),
    nl.

% cas perdu
jeu(BonCode, Nrestant):- 
    Nrestant is 0,
    write('Vous avez perdu !'),
    nl,
    write('Le code était : '),
    write(BonCode),
    nl.

% cas general
jeu(BonCode, Nrestant):-
    Nrestant > 0,
    afficherRestant(Nrestant),
    demanderCode(Code),
    nBienPlace(Code, BonCode, BP),
    nMalPlaces(Code, BonCode, MP),
    afficherBpNp(BP, MP),
    verif(Code, BonCode, Nrestant).

% Lancer la partie
jouons(M, N, Max):-
    codeur(M, N, BonCode),
    jeu(BonCode, Max).