from Grammar import Grammar
from Automaton import FiniteAutomaton

language = {
    'S': ['aF', 'bS'],
    'F': ['bF', 'cD', 'a'],
    'D': ['cS', 'a']
}
# Create an object of the Grammar class
grammar_instance = Grammar(list(language), ['a', 'b', 'c'], language, "S")

# Point A, B: Generate 5 valid strings starting with S
result_strings = grammar_instance.generate_strings(num_strings=5)
print("Point B:")
for string in result_strings:
    print(string)

# Point C: Convert Grammar to FiniteAutomaton
finite_automaton_instance = FiniteAutomaton.grammar_to_DFA(grammar_instance)

print("\nPoint C:")
print("Q:", finite_automaton_instance.Q)
print("Alphabet:", finite_automaton_instance.Alphabet)
print("q0:", finite_automaton_instance.q0)
print("F:",finite_automaton_instance.F)
print("Delta:")
for state, transitions in finite_automaton_instance.delta.items():
    for symbol, result_state in transitions.items():
        print(f"({state}, {symbol}) -> {result_state}")

# Point D: check if the word can be obtained
input_string = "abca"
result = finite_automaton_instance.word_can_be_created(input_string)
print("\nPoint D:")
print(f"The following string '{input_string}' belongs to the language: {result}")