# Variant 1
Vn1 = {'S', 'A', 'B', 'C', 'D', 'E'}
Vt1 = {'a', 'b'}
P1 = {
    'S': ['aB', 'AC'],
    'A': ['a', 'ASC', 'BC', 'aD'],
    'B': ['b', 'bS'],
    'C': ['', 'BA'],
    'D': ['abC'],
    'E': ['aB']
}

# Variant 2
Vn2 = {'S', 'A', 'B', 'C', 'D'}
Vt2 = {'a', 'b'}
P2 = {
    'S': ['aB', 'bA'],
    'A': ['B', 'b', 'aD', 'AS', 'bAAB', ''],
    'B': ['b', 'bS'],
    'C': ['AB'],
    'D': ['BB']
}

# Variant 3
Vn3 = {'S', 'A', 'B', 'C', 'E'}
Vt3 = {'a', 'd'}
P3 = {
    'S': ['dB', 'A'],
    'A': ['d', 'dS', 'aAdAB'],
    'B': ['aC', 'aS', 'AC'],
    'C': [''],
    'E': ['AS']
}