import lexer

python_program = '''
# A program to calculate the factorial of a number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print("Factorial of 5:", result)
'''

lexer_11 = lexer.Lexer(python_program)
tokens = lexer_11.get_tokens()
for token in tokens:
    print(token)
