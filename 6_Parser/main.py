import lexer
from graphviz import Digraph
import AST
import parser_program


def build_graph(node, graph):
    graph.node(str(id(node)), str(node))
    for child in node.children:
        graph.edge(str(id(node)), str(id(child)))
        build_graph(child, graph)



python_program = '''
def calculate_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    return area
    '''

lexer_11 = lexer.Lexer(python_program)
tokens = lexer_11.get_tokens_with_regex()
for token in tokens:
    print(token)

ast = AST.AST.create_ast(tokens)
graph = Digraph()
build_graph(ast, graph)
graph.render('ast_graph', format='png', view=True)
AST.AST.create_ast_method_2(python_program)

python_program = '''
total = total + num
'''
lexer_11 = lexer.Lexer(python_program)
tokens = lexer_11.get_tokens_with_regex()
for token in tokens:
    print(token)

parser = parser_program.Parser(tokens)
parser.parse()