% cas de base
nBienPlace(Code1, Code2, BP) :-
    Code1 = [],
    Code2 = [],
    BP = 0.

% cas recursif positif
nBienPlace(Code1, Code2, BP) :- 
    [T1|R1] = Code1,
    [T2|R2] = Code2,
    T1 = T2,
    nBienPlace(R1, R2, BP2),
    BP is BP2 + 1.

% cas recursif negatif
nBienPlace(Code1, Code2, BP) :- 
    [T1|R1] = Code1,
    [T2|R2] = Code2,
    dif(T1, T2),
    nBienPlace(R1, R2, BP2),
    BP is BP2.

% cas de base
longueur(L, N):-
    L = [],
    N = 0.

% cas recursif
longueur(L, N):-
    [_|R] = L,
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
element(E, L):-
    L = [E|_].

% cas recursif
element(E, L):-
    [T|R] = L,
    dif(T, E),
    element(E, R).

% cas de base
enleve(_, L1, L2):-
    L1 = [],
    L2 = [].

% Debut de liste = premier element de L1
enleve(E, L1, L2):-
    [E|R] = L1,
    R = L2.

% Debut de liste != premier element de L1 (E2), Appel sur R
% et concaténation du resultat de l'appel (Ltemp) avec E2.
enleve(E1, L1, L2):-
    [E2|R] = L1,
    dif(E1, E2),
    enleve(E1, R, Ltemp),
    [E2|Ltemp] = L2.

% cas de base
enleveBP(Code1, Code2, Code1Bis, Code2Bis):-
    Code1 = [],
    Code2 = [],
    Code1Bis = [],
    Code2Bis = [].

% cas premier element identique
enleveBP(Code1, Code2, Code1Bis, Code2Bis):-
    [E1|R1] = Code1,
    [E2|R2] = Code2,
    E1 = E2,
    enleveBP(R1, R2, R1Bis, R2Bis),
    Code1Bis = R1Bis,
    Code2Bis = R2Bis.

% cas premier element different
enleveBP(Code1, Code2, Code1Bis, Code2Bis):-
    [E1|R1] = Code1,
    [E2|R2] = Code2,
    dif(E1,E2),
    enleveBP(R1, R2, R1Bis, R2Bis),
    Code1Bis = [E1|R1Bis],
    Code2Bis = [E2|R2Bis].

% Enlever les BP
nMalPlaces(Code1, Code2, MP):-
    enleveBP(Code1, Code2, Code1Bis, Code2Bis),
    nMalPlacesAux(Code1Bis, Code2Bis, MP).

% cas de base
nMalPlacesAux(Code1, _, MP):-
    Code1 = [],
    MP = 0.

% 1er elt de Code1 dans Code2
nMalPlacesAux(Code1, Code2, MP):-
    [T|R] = Code1,
    element(T, Code2),
    enleve(T, Code2, Code2Bis),
    nMalPlacesAux(R, Code2Bis, MPtemp),
    MP is MPtemp + 1.

% 1er elt de Code1 pas dans Code2
nMalPlacesAux(Code1, Code2, MP):-
    [T|R] = Code1,
    \+ element(T, Code2),
    nMalPlacesAux(R, Code2, MPtemp),
    MP is MPtemp.

% cas de base
codeur(_, N, Code):-
    N is 0,
    Code = [].

% cas général
codeur(M, N, Code):-
    N > 0,
    Nbis is N-1,
    MMax is M+1,
    codeur(M, Nbis, Codetemp),
    random(1, MMax, T),
    Code = [T|Codetemp].

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