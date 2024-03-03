# main.py
from common import Grammar, FiniteAutomaton


grammar = Grammar()
grammar.VN = {'S', 'F', 'D'}
grammar.VT = {'a', 'b', 'c'}
grammar.P = {
    'S': ['aF', 'bS'],
    'F': ['bF', 'cD', 'a'],
    'D': ['cS', 'a']
}

# Check the type of the grammar
print("Grammar Type:", grammar.identify_grammar_type())

# Define the finite automaton variant
finite_automaton = FiniteAutomaton()
finite_automaton.Q = {'q0', 'q1', 'q2', 'q3'}
finite_automaton.Sigma = {'a', 'b', 'c'}
finite_automaton.delta = {('q0', 'b', 'q0'), ('q0', 'a', 'q1'), ('q1', 'c', 'q1'),
                          ('q1', 'a', 'q2'), ('q3', 'a', 'q1'), ('q3', 'a', 'q3'), ('q2', 'a', 'q3')}
finite_automaton.q0 = 'q0'
finite_automaton.F = {'q2'}

# Convert finite automaton to regular grammar
regular_grammar = finite_automaton.to_regular_grammar()

# Print the regular grammar productions
print("\nRegular Grammar Productions for the NDFA:")
productions_output = "\n".join(f"{non_terminal} -> {production}" for non_terminal, productions in regular_grammar.P.items() for production in productions)
print(productions_output)

# Determine if the finite automaton is deterministic
is_deterministic = finite_automaton.is_deterministic()
print("The NDFA is deterministic." if is_deterministic else "The NDFA is non-deterministic.")

# Convert finite automaton to deterministic finite automaton
dfa = finite_automaton.to_deterministic_FiniteAutomaton()

# Check if the resulting DFA is deterministic
is_deterministic_dfa = dfa.is_deterministic()
print("The converted DFA is deterministic." if is_deterministic_dfa else "The converted DFA is non-deterministic.")
