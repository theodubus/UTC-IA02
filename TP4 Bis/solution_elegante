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
    write(' | MP : '),
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


% ================================================== %
% ================= Ajouts TP4 bis ================= %
% ================================================== %

% Joueur : générateur de proposition valides
decodeur(M, N, Hist, Code):-
    gen(M, N, Code),
    test(Hist, Code),
    !.

% Génère une liste d'entiers entre Min et Max
liste_couleurs(Max, Max, [Max]).

liste_couleurs(Min, Max, [Min|Lbis]):-
    Min < Max,
    Min2 is Min + 1,
    liste_couleurs(Min2, Max, Lbis).

% À partir d'une liste, génère la liste incrémentée correspondante
%% Ex : [1, 2, 3] -> [2, 2, 3]
%% Ex : [3, 2, 3] -> [1, 3, 3] si M = 3
incrementer_liste(_, [], []).

incrementer_liste(M, [T|R], [Tbis|R]):-
    T < M,
    Tbis is T + 1.

incrementer_liste(M, [M|R], [1|Lbis]):-
    dif(R, []),
    incrementer_liste(M, R, Lbis).

% Génère une liste de N éléments contenant des 1 (liste de base à incrémenter)
init_liste(0, []).

init_liste(N, [1|Lbis]):-
    N > 0,
    Nbis is N - 1,
    init_liste(Nbis, Lbis).

% Produit la liste des codes possibles
codes(N, M, [L|R]):-
    init_liste(N, L),
    codesAux(M, L, R).

codesAux(M, L, [Linc|Rbis]):-
    incrementer_liste(M, L, Linc),
    codesAux(M, Linc, Rbis).

codesAux(M, L, []):-
    \+ incrementer_liste(M, L, _).

% Utilise la liste des codes possibles pour en faire un générateur
gen(M, N, Code):-
    codes(N, M, Codes),
    member(Code, Codes).

% Historique dont les éléments sont sous la forme [[code], BP, MP]
% Retourne l'historique en ne conservant que les tentatives sans BP ni MP
% Requete test : get_historique([[[1, 1, 1], 1, 2], [[1, 1, 2], 1, 2], [[1, 1, 3], 1, 2], [[1, 2, 1], 1, 2]], Hist).
get_historique([], []).

get_historique([[Code1|_]|R], [Code1|Lbis]):-
    get_historique(R, Lbis).

getBPMP(Code, BonCode, BP, MP):-
    nBienPlace(Code, BonCode, BP),
    nMalPlaces(Code, BonCode, MP).

% Vérifie si un code est valide par rapport à l'historique en comparant les BP et MP
% Requete test : verif_BP_MP([1, 2, 3, 4], [[[1, 2, 3, 4], 4, 0], [[1,1,1,1], 1,0], [[1,3,2,3],1 ,2], [[4,3,2,1], 0,4]]).
verif_BP_MP(_, []).

verif_BP_MP(Code, [[Code1|[BP1|[MP1|[]]]]|R]):-
    getBPMP(Code, Code1, BP1, MP1),
    verif_BP_MP(Code, R).

% Vérifie si un code est valide par rapport à l'historique
% -> non présent dans l'historique et valide par rapport aux BP et MP des codes précédents
% Requete test : test([[[1,5,2,4],1,3],[[4,1,2,4],2,1],[[3,2,1,3],0,2],[[2,2,2,1],1,1],[[1,1,1,1],1,0]], [2,1,5,4]).
test(Historique, Code):-
    get_historique(Historique, Hist_codes),
    \+ member(Code, Hist_codes),
    verif_BP_MP(Code, Historique).


% Partie / tour : cas code invalide
% Requete test : arbitre(5,4,[4,3,2,1],[]).
arbitre(M, N, Code_a_trouver, Hist):-
    longueur(Hist,LH),
    Coups is LH + 1,
    nl,
    write("======================================="), nl,
    write("=============== Tour "), write(Coups), write(" ================"), nl,
    write("======================================="), nl,
    write("Historique : "), write(Hist), nl,
    decodeur(M, N, Hist, Code ),
    \+ gagne(Code_a_trouver, Code),
    getBPMP(Code, Code_a_trouver, BP, MP),
    write("Essai : "), write(Code), nl,
    afficherBpNp(BP, MP),
    arbitre(M, N, Code_a_trouver, [[Code|[BP|[MP|[]]]]|Hist]).

% Cas code valide
arbitre(M, N, Code_a_trouver, Hist) :-
    decodeur(M, N, Hist, Code ),
    gagne(Code_a_trouver, Code),
    longueur(Hist,LH),
    Coups is LH + 1,
    write("Trouvé : "), write(Code), nl,
    write("Gagné en "), write(Coups), write(" coups !"), nl,
    !.

% Lancer une partie avec un codeur humain
partie():-
    write("Nombre de couleurs : "),
    read(M),
    write("Longueur de la combinaison : "),
    read(N),
    write("Code_a_trouver : "),
    read(Code_a_trouver),
    arbitre(M, N, Code_a_trouver, []).

% Lancer une partie avec un codeur bot
partie_bot():-
    write("Nombre de couleurs : "),
    read(M),
    write("Longueur de la combinaison : "),
    read(N),
    codeur(M, N, Code_a_trouver),
    write("Code_a_trouver : "), write(Code_a_trouver), nl,
    arbitre(M, N, Code_a_trouver, []).

    