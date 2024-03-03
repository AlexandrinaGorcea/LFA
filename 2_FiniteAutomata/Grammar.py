import random
# finiteAutomaton.py
from common import FiniteAutomaton


class Grammar:
    def __init__(self):
        self.VN = set()
        self.VT = set()
        self.P = {}

    def generate_strings(self, num_strings=5) -> list:
        ans = []
        while len(ans) < num_strings:
            current_word = self.generate_recursive('S', '')
            if current_word not in ans:
                ans.append(current_word)
        return ans

    def generate_recursive(self, symbol, current_string):
        if symbol in self.VT:
            return current_string + symbol
        else:
            productions = self.P[symbol]
            chosen_production = random.choice(productions)
            for s in chosen_production:
                current_string = self.generate_recursive(s, current_string)
            return current_string

    def to_finite_automaton(self):
        finite_automaton = FiniteAutomaton()

        finite_automaton.Q = self.VN.union(self.VT)
        finite_automaton.Sigma = self.VT
        finite_automaton.delta = set()

        for non_terminal, productions in self.P.items():
            finite_automaton.delta.update(
                (
                    (non_terminal, production[0], production[1])
                    if len(production) > 1
                    else (
                        (non_terminal, production, 'X')
                        if non_terminal in finite_automaton.F or production in {'b', 'd'}
                        else (non_terminal, production, production)
                    )
                )
                for production in productions
            )

        finite_automaton.q0 = 'S'
        finite_automaton.F = {'X'}

        return finite_automaton

    def identify_grammar_type(self):
        start_symbol = next(iter(self.P), None)
        has_epsilon = any('ε' in production for productions in self.P.values() for production in productions)

        for non_terminal, productions in self.P.items():
            for production in productions:
                if len(production) > 2:
                    return "Type-0 (Unrestricted)"
                elif len(production) == 2 and production[0] in self.VN and production[1] in self.VT:
                    return "Type-1 (Context-Sensitive)"
                elif len(production) == 1 and production[0] in self.VT:
                    return "Type-3 (Regular)"

        if start_symbol and not has_epsilon:
            return "Type-2 (Context-Free)"

        return "Type-0 (Unrestricted)"
