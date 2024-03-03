# common.py
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

