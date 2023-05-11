import os

def init_graphe(sommets):
    graphe = {}
    for sommet in sommets:
        graphe[sommet] = []
    return graphe

def ajouter_arete(graphe, sommet1, sommet2):
    graphe[sommet1].append(sommet2)
    graphe[sommet2].append(sommet1)

def creer_graphe_exemple():
    sommets = [i for i in range(1, 11)]
    graphe = init_graphe(sommets)
    ajouter_arete(graphe, 1, 2)
    ajouter_arete(graphe, 1, 3)
    ajouter_arete(graphe, 1, 4)
    ajouter_arete(graphe, 2, 5)
    ajouter_arete(graphe, 2, 9)
    ajouter_arete(graphe, 3, 7)
    ajouter_arete(graphe, 3, 8)
    ajouter_arete(graphe, 4, 6)
    ajouter_arete(graphe, 4, 10)
    ajouter_arete(graphe, 5, 6)
    ajouter_arete(graphe, 5, 8)
    ajouter_arete(graphe, 6, 7)
    ajouter_arete(graphe, 7, 9)
    ajouter_arete(graphe, 8, 10)
    ajouter_arete(graphe, 9, 10)
    return graphe

def convertir_dimacs(graphe):
    couleurs = ["R", "G", "B"]
    sommets = graphe.keys()
    variables = []
    clauses = []
    for sommet in sommets:
        variables_du_sommets = [f"{sommet}{c}" for c in couleurs]
        variables.extend(variables_du_sommets)

    variables_encodees = [i for i in range(1, len(variables) + 1)]

    dict_variables = dict(zip(variables, variables_encodees))
    dict_decode_variables = dict(zip(variables_encodees, variables))

    for sommet in sommets:
        # existence d'une couleur par sommet
        clauses.append(f"{dict_variables[str(sommet) + 'R']} {dict_variables[str(sommet) + 'G']} {dict_variables[str(sommet) + 'B']} 0\n")

        # unicité de la couleur par sommet
        clauses.append(f"-{dict_variables[str(sommet) + 'R']} -{dict_variables[str(sommet) + 'G']} 0\n")
        clauses.append(f"-{dict_variables[str(sommet) + 'R']} -{dict_variables[str(sommet) + 'B']} 0\n")
        clauses.append(f"-{dict_variables[str(sommet) + 'G']} -{dict_variables[str(sommet) + 'B']} 0\n")

        # pas de deux sommets adjacents de la même couleur
        for voisin in graphe[sommet]:
            clauses.append(f"-{dict_variables[str(sommet) + 'R']} -{dict_variables[str(voisin) + 'R']} 0\n")
            clauses.append(f"-{dict_variables[str(sommet) + 'G']} -{dict_variables[str(voisin) + 'G']} 0\n")
            clauses.append(f"-{dict_variables[str(sommet) + 'B']} -{dict_variables[str(voisin) + 'B']} 0\n")

    with open("graphe.cnf", "w") as f:
        f.write(f"p cnf {len(variables)} {len(clauses)}\n")
        f.writelines(clauses)

    return dict_decode_variables
        
def main():
    decode = convertir_dimacs(creer_graphe_exemple())
    output = os.popen("./gophersat graphe.cnf").read()
    solution_line = output.split("\n")[2]
    solution_list = solution_line.split(" ")[1:-1]
    solution_readable = [decode[int(i)] for i in solution_list if int(i) > 0]

    print(f"Solution : {solution_readable}")

if __name__ == "__main__":
    main()