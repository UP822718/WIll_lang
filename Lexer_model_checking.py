from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Parenthesis
        self.lexer.add('OPEN_PAREN'  , r'\(')
        self.lexer.add('CLOSE_PAREN' , r'\)')
        self.lexer.add('OPEN_CURLY'  , r'\{')
        self.lexer.add('CLOSE_CURLY' , r'\}')
        self.lexer.add('OPEN_SQUARE' , r'\[')
        self.lexer.add('CLOSE_SQUARE', r']')

        self.lexer.add('STRUCT' , r'struct')
        self.lexer.add('CLASS'  , r'class')
        self.lexer.add('ACTOR'  , r'actor')
        self.lexer.add('EFFECT' , r'effect')
        self.lexer.add('ENUM'   , r'enum')

        self.lexer.add('CHAR', r'char')
        self.lexer.add('CHAR8', r'char8_t')
        self.lexer.add('CHAR16', r'char16_t')
        self.lexer.add('CHAR32', r'char32_t')
        self.lexer.add('CHARN', r'char([0-9]+)_t')
        self.lexer.add('CONST', r'const')

        self.lexer.add('STATIC_CAST', r'static_cast')
        self.lexer.add('REINTERPRET_CAST', r'reinterpret_cast')
        self.lexer.add('DYNAMIC_CAST', r'dynamic_cast')
        self.lexer.add('RETURN', r'return')
        self.lexer.add('YIELD', r'yield')

        self.lexer.add('GENETIC', r'genetic')
        self.lexer.add('FITNESS', r'fitness')
        self.lexer.add('BEFORE', r'before')
        self.lexer.add('AFTER', r'after')
        self.lexer.add('TRAIN', r'train')
        self.lexer.add('LIFE', r'life')


        self.lexer.add('IN', r'in')
        self.lexer.add('OPTIMISE', r'optimise')
        self.lexer.add('OPTIMISE_SHORT', r'optimise_short')
        self.lexer.add('OPTIMISE_LONG',  r'optimise_long')


        self.lexer.add('IF', r'if')
        self.lexer.add('probability', r'probability')
        self.lexer.add('ELSE', r'else')

        self.lexer.add('GET', r'get')
        self.lexer.add('SET',  r'set')

        self.lexer.add('BOOL'     , r'bool')
        self.lexer.add('INT'      , r'int')
        self.lexer.add('INT8_T'   , r'int8_t')
        self.lexer.add('INT16_T'  , r'int16_t')
        self.lexer.add('INT32_T'  , r'int32_t')
        self.lexer.add('INT64_T'  , r'int64_t')
        self.lexer.add('INTN_T'   , r'int([0-9]+)_t')
        self.lexer.add('UINT4_T'  , r'uint4_t')
        self.lexer.add('UINT8_T'  , r'uint8_t')
        self.lexer.add('UINT16_T' , r'uint16_t')
        self.lexer.add('UINT32_T' , r'uint32_t')
        self.lexer.add('UINT64_T' , r'uint64_t')
        self.lexer.add('UINTN_T'  , r'uint([0-9]+)_t')
        self.lexer.add('SHORT'    , r'short')
        self.lexer.add('TYPE_INFO', r'type_info')
        self.lexer.add('SIGNED'   , r'signed')
        self.lexer.add('STRING'   , r'string')
        self.lexer.add('LONG'     , r'long')
        self.lexer.add('INT'      , r'int')
        self.lexer.add('VOID'     , r'void')
        self.lexer.add('WCHAR_T'  , r'wchar_t')
        ## FF
        self.lexer.add('PROCTYPE', r'proctype')
        self.lexer.add('INIT', r'init')
        self.lexer.add('module', r'module')
        self.lexer.add('formula', r'formula')
        self.lexer.add('rewards', r'rewards')
        self.lexer.add('filter', r'filter')
        self.lexer.add('select', r'select')
        self.lexer.add('process', r'process')
        self.lexer.add('states', r'states')
        self.lexer.add('set', r'set')
        self.lexer.add('read only', r'read only')
        self.lexer.add('from', r'from')
        self.lexer.add('to', r'to')
        self.lexer.add('before', r'before')
        self.lexer.add('after', r'after')
        
        ## WORD
        self.lexer.add('WORD', r'[A-z]+')
        # Ignore spaces
        self.lexer.ignore('\s+')
    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()