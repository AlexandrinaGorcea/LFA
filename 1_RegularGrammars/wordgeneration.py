#Variant 12:
#VN={S, F, D},
#VT={a, b, c},
#P={
#   S → aF
#   F → bF
#   F → cD
#   S → bS
#   D → cS
#   D → a
#   F → a
#}
import random

# Define the grammar
grammar = {
    'S': ['aF', 'bS'],
    'F': ['bF', 'cD', 'a'],
    'D': ['cS', 'a']
}

# Define the function to generate words from the grammar
def generate_word(grammar, symbol):
    if symbol not in grammar:
        return symbol
    production = random.choice(grammar[symbol])
    return ''.join(generate_word(grammar, s) for s in production)

# Generate 5 words from the grammar
for i in range(5):
    word = generate_word(grammar, 'S')
    print(word)
