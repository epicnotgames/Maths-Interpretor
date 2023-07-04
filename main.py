
from lexer import Lexer

while True:
    text = input("math-terperator >> ")
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    print(list(tokens))