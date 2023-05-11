from itertools import combinations

def cell_to_variable(i, j, n):
    return 81 * i + 9 * j + n 

def variable_to_cell(v):
    valeur = (v - 1) % 9 + 1
    ligne = (v - 1) // 81
    colonne = ((v - 1) % 81) // 9
    return ligne, colonne, valeur

def model_to_grid(model):
    grid = [[0 for _ in range(9)] for _ in range(9)]
    for var in model:
        if var > 0:
            ligne, colonne, valeur = variable_to_cell(var)
            grid[ligne][colonne] = valeur
    return grid
    

def at_least_one(liste):
    return liste.copy()

def unique(liste):
    ## combinaisons de 2
    combinaisons = combinations(liste, 2)
    ## liste des clauses
    clauses = []
    clauses.append(at_least_one(liste))
    for combinaison in combinaisons:
        clauses.append([-combinaison[0], -combinaison[1]])
    return clauses


def create_cell_constraints():
    clauses = []
    for i in range(9):
        for j in range(9):
            ## liste des variables
            liste = []
            for n in range(1, 10):
                liste.append(cell_to_variable(i, j, n))
            clauses.extend(unique(liste))
    return clauses


def create_line_constraints():
    clauses = []
    for n in range(1, 10):
        for i in range(9):
            ## liste des variables
            liste = []
            for j in range(9):
                liste.append(cell_to_variable(i, j, n))
            clauses.append(liste)
    return clauses


def create_column_constraints():
    clauses = []
    for n in range(1, 10):
        for j in range(9):
            ## liste des variables
            liste = []
            for i in range(9):
                liste.append(cell_to_variable(i, j, n))
            clauses.append(liste)
    return clauses


def create_box_constraints():
    clauses = []
    for n in range(1, 10):
        for i in range(3):
            for j in range(3):
                ## liste des variables
                liste = []
                for k in range(3):
                    for l in range(3):
                        liste.append(cell_to_variable(3 * i + k, 3 * j + l, n))
                clauses.append(liste)
    return clauses


def create_value_constraints(grid):
    clauses = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                clauses.append([cell_to_variable(i, j, grid[i][j])])
    return clauses


def generate_problem(grid):
    clauses = []
    clauses.extend(create_cell_constraints())
    clauses.extend(create_line_constraints())
    clauses.extend(create_column_constraints())
    clauses.extend(create_box_constraints())
    clauses.extend(create_value_constraints(grid))
    return clauses

def clauses_to_dimacs(clauses, nb_var=729):
    nb_clause = len(clauses)
    chaine = f"p cnf {nb_var} {nb_clause}\n"
    for clause in clauses:
        chaine += " ".join([str(i) for i in clause]) + " 0\n"
    return chaine
    
def display_grid(grid):
    for i in range(25):
        print("-", end="")
    print()
    
    for i in range(9):
        print("|", end=" ")
        for j in range(9):
            n = grid[i][j]
            if n == 0:
                n = "."
            print(n, end=" ")
            if j % 3 == 2:
                print("|", end=" ")
        print()
        if i % 3 == 2:
            for j in range(25):
                print("-", end="")
            print()
    print()
