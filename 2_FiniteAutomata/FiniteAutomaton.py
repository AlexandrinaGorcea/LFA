from functools import reduce
# Grammar.py
from common import Grammar

class FiniteAutomaton:
    def __init__(self):
        self.Q = set()
        self.Sigma = set()
        self.delta = set()
        self.q0 = None
        self.F = set()

    def is_string_in_language(self, input_string):
        def transition(current_state, symbol):
            next_states = {next_state for (state, input_symbol, next_state) in self.delta
                           if state == current_state and input_symbol == symbol}
            return next_states.pop() if next_states else None

        final_state = reduce(transition, input_string, self.q0)
        return final_state in self.F

    def to_regular_grammar(self):
        regular_grammar = Grammar()
        regular_grammar.VN = self.Q
        regular_grammar.VT = self.Sigma
        regular_grammar.P = {state: [] for state in self.Q}

        for state, input_symbol, next_state in self.delta:
            if next_state != 'X':
                production = f"{input_symbol}{next_state}"
                regular_grammar.P[state].append(production)

        return regular_grammar

    def is_deterministic(self):
        visited_states = set()

        for state in self.Q:
            for symbol in self.Sigma:
                next_states = {next_state for (_, input_symbol, next_state) in self.delta
                               if _ == state and input_symbol == symbol}

                if len(next_states) != 1:
                    return False

                visited_states.update(next_states)

        return len(visited_states) == len(self.Q)  # Ensure all states are reachable

    def to_deterministic_FiniteAutomaton(self):
        dfa = FiniteAutomaton()
        dfa.Sigma = self.Sigma
        dfa.q0 = frozenset([self.q0])  # Initial state is the epsilon closure of the original initial state
        dfa.F = set()
        dfa.Q = set([dfa.q0])  # Initialize set of states
        dfa.delta = set()

        # Function to compute epsilon closure of a state in the NFA
        def epsilon_closure(state):
            closure = {state}
            stack = list(state)
            closure.update(next_state for (_, input_symbol, next_state) in self.delta
                           if input_symbol == 'ε' and next_state not in closure)
            return frozenset(closure)

        unprocessed_states = [dfa.q0]

        while unprocessed_states:
            current_state = unprocessed_states.pop(0)

            for symbol in dfa.Sigma:
                next_state = frozenset(
                    next_state
                    for state in current_state
                    for (_, input_symbol, next_state) in self.delta
                    if state in current_state and input_symbol == symbol
                )

                next_state_closure = epsilon_closure(next_state)

                if next_state_closure:
                    dfa.delta.add((current_state, symbol, next_state_closure))

                    if next_state_closure not in dfa.Q:
                        dfa.Q.add(next_state_closure)
                        unprocessed_states.append(next_state_closure)

                    if any(state in self.F for state in next_state_closure):
                        dfa.F.add(next_state_closure)

        return dfa
