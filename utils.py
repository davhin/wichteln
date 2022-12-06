import random, string


def solve(names_constraints):
    givers = list(names_constraints.keys())
    receivers = givers[1:] + [givers[0]]
    givers_receivers = dict(zip(givers, receivers))
    return givers_receivers


def convert_text_to_names(txt):
    names = txt.split(',')
    names = [n.split()[0] for n in names if len(n)>0]
    return names


def get_gift_recipient(recipient_code):
    return "Alice"


def insert_solution_in_db(names_pseudonyms):
    pass


def get_n_random_identifiers(n):
    letters = string.ascii_uppercase
    n_identifiers = []
    for _ in range(n):
        n_identifiers.append(''.join(random.choice(letters) for i in range(5)))
    return n_identifiers