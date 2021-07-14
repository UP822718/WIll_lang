from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        self.lexer.add('OPEN_CURLY', r'\{')
        self.lexer.add('CLOSE_CURLY', r'\}')
        self.lexer.add('OPEN_SQUARE', r'\[')
        self.lexer.add('CLOSE_SQUARE', r']')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        # Operators
        self.lexer.add('Assignment_ADD',r'=\+')  # Done
        self.lexer.add('Assignment_MULT',r'=\*')  # Done
        self.lexer.add('Assignment_SUB',r'=\-')  # Done
        self.lexer.add('Assignment_XOR',r'=\^')  # Done
        self.lexer.add('Assignment_OR',r'=\|')  # Done
        self.lexer.add('Assignment_POWER',r'=\*\*')  # Done
        self.lexer.add('Assignment_Not',r'=\~')  # Done
        self.lexer.add('Assignment_Not',r'=\¬')  # Done
        self.lexer.add('Assignment_AND',r'=\&')  # Done
        self.lexer.add('Assignment',r'=')  # Done

        self.lexer.add('Assignment_ADD_UNSAFE', r'=\+~')  # Done
        self.lexer.add('Assignment_SUB_UNSAFE', r'=\-~')  # Done
        self.lexer.add('Assignment_MUL_UNSAFE', r'=\*~')  # Done
        self.lexer.add('Assignment_DIV_UNSAFE', r'=\/~')  # Done
        self.lexer.add('Assignment_REM_UNSAFE', r'=%~')  # Done
        self.lexer.add('Assignment_MOD_UNSAFE', r'=%%~')  # Done
        self.lexer.add('Assignment_NEG_UNSAFE', r'=-~')  # Done

        self.lexer.add('Assignment_ADD_PARTIAL', r'=\+\?')  # Done
        self.lexer.add('Assignment_SUB_PARTIAL', r'=-\?')  # Done
        self.lexer.add('Assignment_MUL_PARTIAL', r'=\*\?')  # Done
        self.lexer.add('Assignment_DIV_PARTIAL', r'=\\\?')  # Done
        self.lexer.add('Assignment_REM_PARTIAL', r'=%\?')  # Done
        self.lexer.add('COST', r'COST')  # Done
        self.lexer.add('MUT', r'MUT')  # Done

        self.lexer.add('Assignment_MOD_PARTIAL', r'=%%\?')  # Done
        
        self.lexer.add('INCREMENT',r'\+\+') # Done
        self.lexer.add('DECREMENT',r'\-\-') # Done
        self.lexer.add('MULT',r'\*')
        self.lexer.add('POWER',r'\*\*')
        self.lexer.add('DIV',r'\\')
        self.lexer.add('DIV_FLOOR',r'\\\\') # Done

        self.lexer.add('PERCENTAGE',r'%') # Done 
        self.lexer.add('HAT',r'^')        # Done 
        self.lexer.add('AND',r'&')        # Done 
        self.lexer.add('DOT',r'\.')       # Done 
        self.lexer.add('DOT_PONTER',r'->')# Done 
        self.lexer.add('LOGCAL_NOT',r'¬')
        self.lexer.add('SQUIGGLY', r'~')
        self.lexer.add('AT', r'@')

        self.lexer.add('ADD_UNSAFE', r'\+~')    # Done
        self.lexer.add('SUB_UNSAFE', r'\-~')    # Done
        self.lexer.add('MUL_UNSAFE', r'\*~')    # Done
        self.lexer.add('DIV_UNSAFE', r'\/~')    # Done
        self.lexer.add('REM_UNSAFE', r'%~')     # Done
        self.lexer.add('MOD_UNSAFE', r'%%~')    # Done
        self.lexer.add('NEG_UNSAFE', r'-~')     # Done
        self.lexer.add('LT_UNSAFE', r'<~')      # Done
        self.lexer.add('GT_UNSAFE', r'>~')      # Done
        self.lexer.add('LE_UNSAFE', r'<=~')     # Done
        self.lexer.add('GE_UNSAFE', r'>=~')     # Done
        self.lexer.add('EQ_UNSAFE', r'=~')      # Done
        self.lexer.add('NE_UNSAFE', r'!=~')     # Done
        self.lexer.add('ADD_PARTIAL', r'\+\?')  # Done
        self.lexer.add('SUB_PARTIAL', r'-\?')   # Done
        self.lexer.add('MUL_PARTIAL', r'\*\?')  # Done
        self.lexer.add('DIV_PARTIAL', r'\\\?')  # Done
        self.lexer.add('REM_PARTIAL', r'%\?')   # Done
        self.lexer.add('MOD_PARTIAL', r'%%\?')  # Done

        self.lexer.add('EQUAL', r'==') # Done
        self.lexer.add('NOT_EQUAL', r'=!') # Done
        self.lexer.add('GREATER_EQUAL', r'=<') # Done
        self.lexer.add('LESS_EQUAL', r'=>') # Done
        self.lexer.add('PUSH_LEFT', r'<<') # Done
        self.lexer.add('PUSH_RIGHT', r'>>') # Done

        self.lexer.add('STACK','stack') #one
        self.lexer.add('QUEUE','queue') #one
        self.lexer.add('DEQUE','deque') #one
        self.lexer.add('RING ','ring') #one
        self.lexer.add('ALIST','alist') #one
        self.lexer.add('SKIP','skip') #one

        self.lexer.add('DOLLOR', r'$')
        self.lexer.add('QUESTION', r'\?')
        self.lexer.add('HORIZONTAL_BAR', r'\|')  
        self.lexer.add('BANG', r'!')

        self.lexer.add('LESS', r'<')
        self.lexer.add('GREATER', r'>')

        self.lexer.add('ISO', r'iso')  # Done 
        self.lexer.add('VAL', r'val')  # Done 
        self.lexer.add('REF', r'ref')  # Done 
        self.lexer.add('BOX', r'box')  # Done 
        self.lexer.add('TRN', r'trn')  # Done 
        self.lexer.add('TAG', r'tag')  # Done 

        self.lexer.add('CONSUME', r'consume') # Done
        self.lexer.add('ALIGNAS', r'alignas')
        self.lexer.add('alignof', r'alignof')
        self.lexer.add('SEMAPHORE', r'semaphore')
        self.lexer.add('container', r'container')
        self.lexer.add('ARRAY', r'array') # done 
        self.lexer.add('UNION', r'union') # done 
        self.lexer.add('ALGEBRAIC', r'algebraic')
        self.lexer.add('MAP', r'map') # done 
        self.lexer.add('dependent', r'dependent')
        self.lexer.add('list', r'list')
        self.lexer.add('atomic_noexcept', r'atomic_noexcept')
        self.lexer.add('atomic_cancel', r'atomic_cancel')
        self.lexer.add('atomic_commit', r'atomic_commit')
        self.lexer.add('synchronized', r'synchronized')
        self.lexer.add('BREAK', r'break')
        self.lexer.add('CASE', r'case')
        self.lexer.add('CHAR', r'char')             # Done 
        self.lexer.add('CHAR8', r'char8_t')         # Done 
        self.lexer.add('CHAR16', r'char16_t')       # Done 
        self.lexer.add('CHAR32', r'char32_t')       # Done 
        self.lexer.add('CHARN', r'char([0-9]+)_t')  # Done 
        self.lexer.add('GET', r'get')              # Done 
        self.lexer.add('SET',  r'set')              # Done 
        self.lexer.add('BOOL', r'bool')              # Done 
        self.lexer.add('INT',  r'int')               # Done 
        self.lexer.add('INT8_T',  r'int8_t')         # Done 
        self.lexer.add('INT16_T', r'int16_t')        # Done 
        self.lexer.add('INT32_T', r'int32_t')        # Done 
        self.lexer.add('INT64_T', r'int64_t')        # Done 
        self.lexer.add('INTN_T', r'int([0-9]+)_t')   # Done 
        self.lexer.add('UINT4_T',  r'uint4_t')       # Done 
        self.lexer.add('UINT8_T',  r'uint8_t')       # Done 
        self.lexer.add('UINT16_T', r'uint16_t')      # Done 
        self.lexer.add('UINT32_T', r'uint32_t')      # Done 
        self.lexer.add('UINT64_T', r'uint64_t')      # Done 
        self.lexer.add('UINTN_T', r'uint([0-9]+)_t') # Done 
        self.lexer.add('VOID', r'void')       # Done
        self.lexer.add('WCHAR_T', r'wchar_t') # Done
        self.lexer.add('COMPL', r'compl')
        self.lexer.add('CONCEPT', r'concept')
        self.lexer.add('CONST', r'const')
        self.lexer.add('CONTINUE', r'continue')
        self.lexer.add('AWAIT', r'await')
        self.lexer.add('RETURN', r'return')# Done 
        self.lexer.add('YIELD', r'yield')  # Done 
        self.lexer.add('NEW', r'new')
        self.lexer.add('NAMESPACE', r'namespace')
        self.lexer.add('MUTABLE', r'mutable')
        self.lexer.add('INLINE', r'inline')
        self.lexer.add('IF', r'if')     # Done 
        self.lexer.add('FOR', r'for')   # Done 
        self.lexer.add('ELSE', r'else') # Done 
        self.lexer.add('friend', r'friend')
        self.lexer.add('IN', r'in') # Done 
        self.lexer.add('OPTIMISE', r'optimise') # Done
        self.lexer.add('constraint',  r'constraint')
        self.lexer.add('FLOAT', r'float') # DONE
        self.lexer.add('DOUBLE', r'double') # DONE
        self.lexer.add('DELETE', r'delete') # DONE
        self.lexer.add('DEFAULT', r'default')
        self.lexer.add('AUTO', r'auto') # Done
        self.lexer.add('requires', r'requires')
        self.lexer.add('sizeof', r'sizeof') # Done
        self.lexer.add('STATIC', r'static')
        self.lexer.add('STATIC_CAST', r'static_cast') # Done
        self.lexer.add('REINTERPRET_CAST', r'reinterpret_cast') # Done
        self.lexer.add('DYNAMIC_CAST', r'dynamic_cast') # Done
        self.lexer.add('CONSTEVAL', r'consteval')
        self.lexer.add('CONSTEXPR', r'constexpr')
        self.lexer.add('CONSTINIT', r'constinit')
        self.lexer.add('CONST_CAST', r'const_cast')  # Done

        self.lexer.add('STRUCT', r'struct') # Done
        self.lexer.add('CLASS', r'class')   # Done
        self.lexer.add('ACTOR', r'actor')   # Done
        self.lexer.add('EFFECT', r'effect') # Done
        self.lexer.add('ENUM', r'enum')     # Done
        self.lexer.add('SWITCH', r'switch') # done 
        self.lexer.add('THIS', r'this') # Done
        self.lexer.add('ME', r'me') # Done+-``
        self.lexer.add('THREAD_LOCAL', r'thread_local')
        self.lexer.add('THROW', r'throw')  # done
        self.lexer.add('TRUE', r'true')    # done 
        self.lexer.add('FALSE', r'false')  # done 

        self.lexer.add('TRY', r'try') # done 
        self.lexer.add('CATCH', r'catch') # done 

        self.lexer.add('TYPEDEF', r'typedef')
        self.lexer.add('TYPEID', r'typeid')
        self.lexer.add('TYPENAME', r'typename')
        self.lexer.add('UNSIGNED', r'unsigned')
        self.lexer.add('using', r'using')
        self.lexer.add('virtual', r'virtual')
        self.lexer.add('WHILE', r'while')
        self.lexer.add('COLON', r':')
        self.lexer.add('COMMAR', r',')
        self.lexer.add('LET', r'let')

        self.lexer.add('GENETIC', r'genetic') # DONE
        self.lexer.add('FITNESS', r'fitness') # DONE
        self.lexer.add('BEFORE', r'before')   # DONE
        self.lexer.add('AFTER', r'after')     # DONE
        self.lexer.add('TRAIN', r'train')     # DONE
        self.lexer.add('LIFE', r'life')       # DONE


        self.lexer.add('IMPORT', r'#import') # DONE
        self.lexer.add('INCLUDE_LOCAL', r'#include_local') # DONE
        self.lexer.add('INCLUDE', r'#include') # DONE
        self.lexer.add('LABEL', r'#label') # DONE
        # Number
        self.lexer.add('NUMBER_INT', r'\d+')      # Done  
        self.lexer.add('NUMBER_FLOAT', r'd+\.d+') # Done 
        self.lexer.add('NUMBER_FLOAT', r'\.d+')   # Done 
        self.lexer.add('SUPERSCRIPT', r'[⁺|⁻]([⁰|¹|²|³|⁴|⁵|⁶|⁷|⁸|⁹]+)')
        self.lexer.add('FRACTION', r'[¼|½|¾|⅐|⅑|⅒|⅓|⅔|⅕|⅖|⅗|⅘|⅙|⅚|⅛|⅜|⅝|⅞]')
        ## STRING
        self.lexer.add('literal_string', r'"(.+?)"')  # Done 
        self.lexer.add('literal_string', r'`(.+?)`')  # Done 
        self.lexer.add('literal_string', r"'(.+?)'")  # Done 
        self.lexer.add('literal_string_empty', r'""') # Done 
        self.lexer.add('literal_string_empty', r'``') # Done 
        self.lexer.add('literal_string_empty', r"''") # Done 
        ## debug
        self.lexer.add('debug_assert', r"debug_assert")
        self.lexer.add('debug_static_assert', r"debug_static_assert")
        self.lexer.add('debug_assume', r"debug_assume")
        self.lexer.add('debug_cover', r"debug_cover")
        self.lexer.add('debug_label', r"debug_label")
        self.lexer.add('debug_error', r"debug_error")
        self.lexer.add('debug_atomic_begin', r"debug_atomic_begin")
        self.lexer.add('debug_atomic_end', r"debug_atomic_end")
        self.lexer.add('debug_trace_print', r"debug_trace_print")
        ## WORD
        self.lexer.add('WORD', r'[A-z]+')
        # Ignore spaces
        self.lexer.ignore('\s+')
    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()