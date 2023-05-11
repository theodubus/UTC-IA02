def decomp2(n : int, nb_bits : int):
    decomposition = list()
    
    for _ in range(nb_bits):
        decomposition.append(n%2 == 1)
        n //= 2

    return decomposition[::-1]


def decomp(n : int, nb_bits : int):
    str_binary = str(bin(n)[2:])
    zeroes = list()

    if len(str_binary) < nb_bits:
        bits_to_add = nb_bits - len(str_binary)
        zeroes = [False for _ in range(bits_to_add)]
    
    str_binary.split()
    decomposition = [str_binary[i] == "1" for i in range(len(str_binary))]

    return zeroes + decomposition


def interpretation(voc: list[str], vals: list[bool]):
    return {k: v for k, v in zip(voc, vals)}


def gen_interpretations(voc: list[str]):
    nb_bits = len(voc)
    n = 2**nb_bits

    for i in range(n):
        vals = decomp(i, nb_bits)
        yield interpretation(voc, vals)


def valuate(formula: str, interpretation: dict[str, bool]):
    return eval(formula, interpretation)

def transform(val : bool):
    if val:
        return 'T'
    return 'F'

def affichage(formule, voc):
    print(f"formule : {formule}\n")

    g = gen_interpretations(voc)

    for variable in voc:
        print(f"+-{'-'*len(variable)}-", end="")
    print("+-------+")

    for variable in voc:
        print(f"| {variable} ", end="")
    print("|", end="")
    print(" eval. |")

    for variable in voc:
        print(f"+-{'-'*len(variable)}-", end="")
    print("+-------+")

    

    for interpretation in g:
        res = valuate(formule, interpretation)

        for variable, variable_res in enumerate(list(interpretation.values())[:len(voc)]):
            print(f"| {transform(variable_res):<{len(voc[variable])}} ", end="")
        
        print("|", end="")

        print(f"   {transform(res)}   |")

    for variable in voc:
        print(f"+-{'-'*len(variable)}-", end="")
    print("+-------+")


def nature(formule, voc):
    g = gen_interpretations(voc)

    existe_vrai = False
    existe_faux = False
    
    for interpretation in g:
        if valuate(formule, interpretation):
            existe_vrai = True
        else:
            existe_faux = True


    if existe_vrai and existe_faux:
        return "Contingente"
    elif existe_vrai:
        return "Valide"
    else:
        return "Contradictoire"
    

def contingence(formule, voc):
    return nature(formule, voc) == "Contingente"

def validite(formule, voc):
    return nature(formule, voc) == "Valide"

def contradiction(formule, voc):
    return nature(formule, voc) == "Contradictoire"



def test(nb_variables):
    n = nb_variables
    variables = [f"X{i}" for i in range(1, n+1)]

    formule = ""
    for i in range(1, n):
        formule += f"(X{i} or X{i+1}) and "

    formule = formule[:-5]

    print(f"nb variables : {n}")
    print(nature(formule, variables))

    # affichage(formule, variables)

def is_cons(f1: str, f2: str, voc: list[str]):
    """
    Détermine si f1 => f2
    """
    formula = f"not ({f1}) or {f2}"
    res = validite(formula, voc)
    print(f"\"{f1} => {f2}\" is {res}")
    return res

is_cons("X1 and X3", "X1 or X3 and X2", ["X1", "X2", "X3"])
affichage("X1 or X3 and X2", ["X1", "X2", "X3"])
