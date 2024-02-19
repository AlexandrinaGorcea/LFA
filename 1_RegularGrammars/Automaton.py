from Grammar import Grammar

class FiniteAutomaton:
    def __init__(self, grammar: Grammar, _delta: dict) -> None:
        self.Q = grammar.nonterminals + ["X"]
        self.Alphabet = grammar.terminals
        self.q0 = grammar.start
        self.delta = _delta
        self.F = ["X"]

    def grammar_to_DFA(grammar: Grammar) -> 'FiniteAutomaton':
        delta = {}

        for nonterminal in grammar.language:
            for production in grammar.language[nonterminal]:
                if len(production) > 1:
                    transition = production[0]
                    result_state = production[1]
                    delta.setdefault(nonterminal, {})[transition] = result_state
                else:
                    transition = production
                    result_state = "X"
                    delta.setdefault(nonterminal, {})[transition] = result_state

        return FiniteAutomaton(grammar, delta)

    def word_can_be_created(self, string: str) -> bool:
        current_state = self.q0

        for char in string:
            if char not in self.Alphabet or char not in self.delta[current_state]:
                return False
            current_state = self.delta[current_state][char]

        return current_state in self.F
