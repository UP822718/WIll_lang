from Lexer import Lexer
from Parser import Parser

text_input = """
actor HELLO {
    box bool hi;
    
    box void test(){}
 }
"""


lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
for i in tokens:
    print(i)

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
print("name:" ,parser.parse(tokens).next.name)