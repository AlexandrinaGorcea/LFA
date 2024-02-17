import random

# Define the grammar
grammar = {
    'S': ['aF', 'bS'],
    'F': ['bF', 'cD', 'a'],
    'D': ['cS', 'a']
}

# Define a function to convert the grammar to a finite automaton
def grammar_to_finite_automaton(grammar):
    # Define the set of states as the nonterminal symbols in the grammar, plus a special start state
    states = set(grammar.keys()) | {'S0'}

    # Define the input alphabet as the set of terminal symbols in the grammar
    alphabet = set([s for rule in grammar.values() for s in rule if s.islower()])

    # Define the transition function
    transitions = {}
    for state in states:
        for symbol in alphabet:
            # If the symbol is not in any rule, the transition goes to a dead state
            dest_state = 'dead'
            for rule in grammar.get(state, []):
                if symbol in rule:
                    # If the symbol is in a rule, the transition goes to the state associated with that rule
                    dest_state = ''.join([s if s.isupper() else '' for s in rule])
            transitions[(state, symbol)] = dest_state

    # Define the start state as the special start state
    start_state = 'S0'

    # Define the set of accept states as the nonterminal symbols that can generate a word
    accept_states = set(state for state in states if any(word == state for word in generate_word(grammar, 'S')))

    # Return the finite automaton
    return (states, alphabet, transitions, start_state, accept_states)


# Define a function to generate words from the grammar
def generate_word(grammar, symbol):
    if symbol not in grammar:
        return symbol
    production = random.choice(grammar[symbol])
    return ''.join(generate_word(grammar, s) for s in production)


# Test the conversion function
fa = grammar_to_finite_automaton(grammar)
print(fa)