from rply import ParserGenerator
from ast import  *
class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            [
                "ISO",
                "VAL",
                "REF",
                "BOX",
                "TRN",
                "TAG",
                "STRUCT",
                "CLASS",
                "ACTOR",
                "EFFECT",
                "ENUM",
                "WORD",
                "OPEN_CURLY",
                "$end",
                "ISO",
                "VAL",
                "REF",
                "TRN",
                "TAG",
                "ARRAY",
                "NAME",
                "WCHAR_T",
                "VOID",
                "STRING",
                "VOID",
                "CHAR",
                "CHAR8",
                "CHAR16",
                "CHAR32",
                "BOOL",
                "AUTO",
                "INT",
                "LONG",
                "LONG",
                "LONG",
                "SHORT",
                "FLOAT",
                "DOUBLE",
                "INT8_T",
                "INT16_T",
                "INT32_T",
                "INT64_T",
                "INTN_T",
                "UINT4_T",
                "UINT8_T",
                "UINT16_T",
                "UINT32_T",
                "UINT64_T",
                "UINTN_T",
                "STRING",
                "SIGNED",
                "UNSIGNED",
                "STRING",
                "SEMI_COLON",
                "OPTIMISE_LONG",
                "OPTIMISE_SHORT",
                "OPTIMISE",
                "LIFE",
                "COLON",
                "BEFORE",
                "ALTER",
                "FITNESS",
                "CLOSE_CURLY",
                'VOID',
                'CHAR',
                'CHAR8',
                'CHAR16',
                'STACK',
                'QUEUE',
                'DEQUE',
                'RING',
                'ALIST',
                'LIST',
                'SKIP',
                'CHAR32',
                'BOOL',
                'AUTO',
                'INT',
                'LONG',
                'SHORT',
                'FLOAT',
                'DOUBLE',
                'UNSIGNED',
                'SIGNED',
                'INT8_T',
                'INT16_T',
                'INT32_T',
                'INT64_T',
                'INTN_T',
                'UINT4_T',
                'UINT8_T',
                'UINT16_T',
                'UINT32_T',
                'UINT64_T',
                'UINTN_T',
                'STRING',
                'VOID',
                'WCHAR_T',
                "Assignment_ADD",
                "Assignment_MULT",
                "Assignment_SUB",
                "Assignment_XOR",
                "Assignment_OR",
                "Assignment_POWER",
                "Assignment_Not",
                "Assignment_AND",
                "Assignment",
                "GREATER",
                "LESS",
                "HORIZONTAL_BAR",
                "PUSH_RIGHT",
                "PUSH_LEFT",
                "LESS_EQUAL",
                "GREATER_EQUAL",
                "NOT_EQUAL",
                "AND",
                "HAT",
                "DIV_FLOOR",
                "MULT",
                "PERCENTAGE",
                "DIV",
                "POWER",
                "DYNAMIC_CAST",
                "REINTERPRET_CAST",
                "STATIC_CAST",
                "NUMBER_INT",
                "NUMBER_FLOAT",
                "NUMBER_FLOAT",
                "FRACTION",
                "literal_string",
                "literal_string_empty",
                "TRUE",
                "FALSE",
                "COMMAR",
                "RETURN",
                "YIELD",
                "IF",
                "FOR",
                "OPEN_PAREN",
                "CLOSE_PAREN",
                "OPEN_SQUARE",
                "CLOSE_SQUARE",
                "FOR",
                "ELSE",
                "AT",
                "$end",
                "ADD_UNSAFE",
                "SUB_UNSAFE",
                "MUL_UNSAFE",
                "DIV_UNSAFE",
                "REM_UNSAFE",
                "MOD_UNSAFE",
                "NEG_UNSAFE",
                "LT_UNSAFE",
                "GT_UNSAFE",
                "LE_UNSAFE",
                "GE_UNSAFE",
                "EQ_UNSAFE",
                "NE_UNSAFE",
                "ADD_PARTIAL",
                "SUB_PARTIAL",
                "MUL_PARTIAL",
                "DIV_PARTIAL",
                "REM_PARTIAL",
                "MOD_PARTIAL",
                "TRY",
                "GENETIC",
                "SWITCH",
                "CASE",
                "DEFAULT",
                "BREAK",
                "CONSUME",
                "DECREMENT",
                "INCREMENT",
                "IN",
                "SET",
                "LABEL",
                "LINE",
                "INCLUDE_LOCAL",
                "INCLUDE",
                "LABEL",
                "GET",
                "literal_string",
                "IMPORT",
                "DOT_PONTER",
                "DOT",
                "MAP",
                "DELETE",
                "SIZEOF",
                "CATCH",
                "CONST_CAST",
                "ME",
                "THIS",
                "MULT",
                "COST"
            ]
        )
        # directive
    def parse(self):
        @self.pg.production('program : complex program')
        def directive_start (p):
            return PROGRAM(p[0])
        @self.pg.production('obj_name : NAME DOT obj_name')
        @self.pg.production('obj_name : NAME DOT_PONTER obj_name')
        def directive_code (p):
            pass
        @self.pg.production('obj_name : NAME SEMI_COLON')
        def directive_code (p):
            pass


        @self.pg.production('program : IMPORT literal_string')
        @self.pg.production('program : INCLUDE_LOCAL literal_string')
        @self.pg.production('program : INCLUDE literal_string')
        @self.pg.production('program : LINE literal_string')
        @self.pg.production('program : LABEL literal_string')
        @self.pg.production('program : IMPORT literal_string')
        def directive_code (p):
            print("end of program")
            inside = p[0]
            name = p[1]
            if inside.gettokentype() == 'IMPORT':
                return IMPORT(name)
            if inside.gettokentype() == 'INCLUDE_LOCAL':
                return INCLUDE_LOCAL(name)
            if inside.gettokentype() == 'INCLUDE':
                return INCLUDE(name)
            if inside.gettokentype() == 'LINE':
                return LINE(name)
            if inside.gettokentype() == 'LABEL':
                return LABEL(name)
    

        @self.pg.production('program : $end')
        def directive_start (p):
            print("end of program")
            return PROGRAM_END()

        @self.pg.production('capabilities : ISO')
        @self.pg.production('capabilities : VAL')
        @self.pg.production('capabilities : REF')
        @self.pg.production('capabilities : TRN')
        @self.pg.production('capabilities : TAG')
        @self.pg.production('capabilities : BOX')
        @self.pg.production('capabilities : COST')
        def capabilities (p):
            print("capabilities")
            inside = p[0]
            if inside.gettokentype() == 'ISO':
                return ISO()
            elif inside.gettokentype() == 'VAL':
                return VAL()
            elif inside.gettokentype() == 'REF':
                return REF()
            elif inside.gettokentype() == 'TRN':
                return TRN()
            elif inside.gettokentype() == 'TAG':
                return TAG()
            elif inside.gettokentype() == 'BOX':
                return BOX() 
            elif inside.gettokentype() == 'COST':
                return COST() 
        @self.pg.production('enum_start : COMMAR NAME enum_start')
        def datatype (p):
            pass
        @self.pg.production('enum_start : COMMAR NAME Assignment complex enum_start')
        @self.pg.production('enum_start : COMMAR NAME Assignment expression enum_start')
        def datatype (p):
            pass
        @self.pg.production('enum_start : COMMAR NAME ')
        def datatype (p):
            pass

        @self.pg.production('datatype : ARRAY datatype')
        @self.pg.production('datatype : LIST datatype')
        @self.pg.production('datatype : REF datatype')
        @self.pg.production('datatype : STACK datatype')
        @self.pg.production('datatype : QUEUE datatype')
        @self.pg.production('datatype : DEQUE datatype')
        @self.pg.production('datatype : RING datatype')
        @self.pg.production('datatype : ALIST datatype')
        @self.pg.production('datatype : SKIP  datatype')
        def datatype (p):
            print("datatype")
            inside = p[0]
            if inside.gettokentype() == "ARRAY":
                return ARRAY(p[1])
            if inside.gettokentype() == "LIST":
                return LIST(p[1])
            if inside.gettokentype() == "REF":
                return REF(p[1])
            if inside.gettokentype() == "STACK":
                return STACK(p[1])
            if inside.gettokentype() == "QUEUE":
                return QUEUE(p[1])
            if inside.gettokentype() == "DEQUE":
                return DEQUE(p[1])
            if inside.gettokentype() == "RING":
                return RING(p[1])
            if inside.gettokentype() == "ALIST":
                return ALIST(p[1])
            if inside.gettokentype() == "SKIP":
                return SKIP(p[1])
        @self.pg.production('datatype : STACK OPEN_SQUARE NUMBER_INT CLOSE_SQUARE datatype')
        @self.pg.production('datatype : QUEUE OPEN_SQUARE NUMBER_INT CLOSE_SQUARE datatype')
        @self.pg.production('datatype : DEQUE OPEN_SQUARE NUMBER_INT CLOSE_SQUARE datatype')
        @self.pg.production('datatype : RING OPEN_SQUARE NUMBER_INT CLOSE_SQUARE datatype')
        @self.pg.production('datatype : RING OPEN_SQUARE NUMBER_INT CLOSE_SQUARE datatype')
        @self.pg.production('datatype : SKIP OPEN_SQUARE NUMBER_INT CLOSE_SQUARE datatype')
        @self.pg.production('datatype : ARRAY OPEN_SQUARE NUMBER_INT CLOSE_SQUARE datatype')
        @self.pg.production('datatype : LIST  OPEN_SQUARE NUMBER_INT CLOSE_SQUARE datatype')
        def datatype (p):
            print("datatype")
            inside = p[0]
            if inside.gettokentype() == "ARRAY":
                return ARRAY(p[1],p[2],p[4])
            if inside.gettokentype() == "LIST":
                return LIST(p[1],p[2],p[4])
            if inside.gettokentype() == "REF":
                return REF(p[1],p[2],p[4])
            if inside.gettokentype() == "STACK":
                return STACK(p[1],p[2],p[4])
            if inside.gettokentype() == "QUEUE":
                return QUEUE(p[1],p[2],p[4])
            if inside.gettokentype() == "DEQUE":
                return DEQUE(p[1],p[2],p[4])
            if inside.gettokentype() == "RING":
                return RING(p[1],p[2],p[4])
            if inside.gettokentype() == "ALIST":
                return ALIST(p[1],p[2],p[4])
            if inside.gettokentype() == "SKIP":
                return SKIP(p[1],p[2],p[4])
        @self.pg.production('datatype : MAP LESS complex datatype COMMAR complex datatype GREATER')
        def datatype_MAP (p):
            return MAP(p[2],p[3],p[5],p[6])

        @self.pg.production('datatype : VOID')
        @self.pg.production('datatype : CHAR')
        @self.pg.production('datatype : CHAR8')
        @self.pg.production('datatype : CHAR16')
        @self.pg.production('datatype : CHAR32')
        @self.pg.production('datatype : BOOL')
        @self.pg.production('datatype : AUTO')
        @self.pg.production('datatype : INT')
        @self.pg.production('datatype : LONG')
        @self.pg.production('datatype : SHORT')
        @self.pg.production('datatype : FLOAT')
        @self.pg.production('datatype : DOUBLE')
        @self.pg.production('datatype : UNSIGNED')
        @self.pg.production('datatype : SIGNED')
        @self.pg.production('datatype : INT8_T')
        @self.pg.production('datatype : INT16_T')
        @self.pg.production('datatype : INT32_T')
        @self.pg.production('datatype : INT64_T')
        @self.pg.production('datatype : INTN_T')
        @self.pg.production('datatype : UINT4_T')
        @self.pg.production('datatype : UINT8_T')
        @self.pg.production('datatype : UINT16_T')
        @self.pg.production('datatype : UINT32_T')
        @self.pg.production('datatype : UINT64_T')
        @self.pg.production('datatype : UINTN_T')
        @self.pg.production('datatype : STRING')
        @self.pg.production('datatype : AUTO')
        @self.pg.production('datatype : VOID')
        @self.pg.production('datatype : WCHAR_T')
        @self.pg.production('datatype : NAME')
        def datatype (p):
            print("datatype")
            inside = p[0]
            if inside.gettokentype() == "VOID":
                return VOID()
            elif inside.gettokentype() == "CHAR":
                return CHAR()
            elif inside.gettokentype() == "CHAR8":
                return CHAR8()
            elif inside.gettokentype() == "CHAR16":
                return CHAR16()
            elif inside.gettokentype() == "CHAR32":
                return CHAR32()
            elif inside.gettokentype() == "BOOL":
                return BOOL()
            elif inside.gettokentype() == "AUTO":
                return AUTO()
            elif inside.gettokentype() == "INT":
                return INT()
            elif inside.gettokentype() == "LONG":
                return LONG()
            elif inside.gettokentype() == "LONG_INT":
                return LONG_INT()
            elif inside.gettokentype() == "LONG_LONG":
                return LONG_LONG()
            elif inside.gettokentype() == "SHORT":
                return SHORT()
            elif inside.gettokentype() == "FLOAT":
                return FLOAT()
            elif inside.gettokentype() == "DOUBLE":
                return DOUBLE()
            elif inside.gettokentype() == "INT8_T":
                return INT8_T()
            elif inside.gettokentype() == "INT16_T":
                return INT16_T()
            elif inside.gettokentype() == "INT32_T":
                return INT32_T()
            elif inside.gettokentype() == "INT64_T":
                return INT64_T()
            elif inside.gettokentype() == "INTN_T":
                return INTN_T()
            elif inside.gettokentype() == "UINT4_T":
                return UINT4_T()
            elif inside.gettokentype() == "UINT8_T":
                return UINT8_T()
            elif inside.gettokentype() == "UINT16_T":
                return UINT16_T()
            elif inside.gettokentype() == "UINT32_T":
                return UINT32_T()
            elif inside.gettokentype() == "UINT64_T":
                return UINT64_T()
            elif inside.gettokentype() == "UINTN_T":
                return UINTN_T()
            elif inside.gettokentype() == "STRING":
                return STRING()
            elif inside.gettokentype() == "VOID":
                return VOID()
            elif inside.gettokentype() == "WCHAR_T":
                return WCHAR_T()
            elif inside.gettokentype() == "AUTO":
                return AUTO()
        
        @self.pg.production('complex : STRUCT WORD OPEN_CURLY struct_next')
        @self.pg.production('complex : CLASS WORD OPEN_CURLY class_next')
        @self.pg.production('complex : interface WORD OPEN_CURLY interface_next')
        @self.pg.production('complex : ACTOR WORD OPEN_CURLY actor_next')
        @self.pg.production('complex : EFFECT WORD OPEN_CURLY  effect_next')
        @self.pg.production('complex : ENUM WORD OPEN_CURLY enum_start')
        @self.pg.production('complex : TRAIT WORD OPEN_CURLY trait_start')
        @self.pg.production('complex : UNION WORD OPEN_CURLY union_start')
        @self.pg.production('complex : STRATEGY WORD OPEN_CURLY strategy_start')
        def directive_start (p):
            inside = p[0]
            name = p[1]
            insides = None #p[4]
            if inside.gettokentype() == 'STRUCT':
                return STRUCT(name,None,insides)
            elif inside.gettokentype() == 'CLASS':
                return CLASS(name,None,insides)
            elif inside.gettokentype() == 'ACTOR':
                return ACTOR(name,None,insides)
            elif inside.gettokentype() == 'EFFECT':
                return EFFECT(name,None,insides)
            elif inside.gettokentype() == 'ENUM':
                return ENUM(name,None,insides)
        @self.pg.production('strategy_next :   LET WORD COLON datatype SEMI_COLON strategy_next')
        @self.pg.production('interface_next :  LET WORD COLON datatype SEMI_COLON interface_next')
        @self.pg.production('actor_next :      LET WORD COLON datatype SEMI_COLON actor_next')
        @self.pg.production('effect_next :     LET WORD COLON datatype SEMI_COLON effect_next')
        @self.pg.production('union_start :     LET WORD COLON datatype SEMI_COLON union_start')
        def let_datatype (p):
            pass
        @self.pg.production('struct_next :     LET WORD Assignment expression SEMI_COLON struct_next')
        @self.pg.production('interface_next :  LET WORD Assignment expression SEMI_COLON interface_next')
        @self.pg.production('actor_next :      LET WORD Assignment expression SEMI_COLON actor_next')
        @self.pg.production('effect_next :     LET WORD Assignment expression SEMI_COLON effect_next')
        @self.pg.production('union_start :     LET WORD Assignment expression SEMI_COLON union_start')
        def let_assignment (p):
            pass
        @self.pg.production('struct_next :     LET WORD COLON datatype Assignment expression SEMI_COLON struct_next')
        @self.pg.production('interface_next :  LET WORD COLON datatype Assignment expression SEMI_COLON interface_next')
        @self.pg.production('actor_next :      LET WORD COLON datatype Assignment expression SEMI_COLON actor_next')
        @self.pg.production('effect_next :     LET WORD COLON datatype Assignment expression SEMI_COLON effect_next')
        @self.pg.production('union_start :     LET WORD COLON datatype Assignment expression SEMI_COLON union_start')
        def let_datatype_assignment (p):
            pass
        @self.pg.production('strategy_next :   VAR WORD COLON datatype SEMI_COLON strategy_next')
        @self.pg.production('struct_next :     VAR WORD COLON datatype SEMI_COLON struct_next')
        @self.pg.production('interface_next :  VAR WORD COLON datatype SEMI_COLON interface_next')
        @self.pg.production('actor_next :      VAR WORD COLON datatype SEMI_COLON actor_next')
        @self.pg.production('effect_next :     VAR WORD COLON datatype SEMI_COLON effect_next')
        @self.pg.production('union_start :     VAR WORD COLON datatype SEMI_COLON union_start')
        def var_datatype (p):
            pass
        @self.pg.production('struct_next :     VAR WORD Assignment expression SEMI_COLON struct_next')
        @self.pg.production('interface_next :  VAR WORD Assignment expression SEMI_COLON interface_next')
        @self.pg.production('actor_next :      VAR WORD Assignment expression SEMI_COLON actor_next')
        @self.pg.production('effect_next :     VAR WORD Assignment expression SEMI_COLON effect_next')
        @self.pg.production('union_start :     VAR WORD Assignment expression SEMI_COLON union_start')
        def var_Assignment(p):
            pass
        @self.pg.production('struct_next :     VAR WORD COLON datatype Assignment expression SEMI_COLON struct_next')
        @self.pg.production('interface_next :  VAR WORD COLON datatype Assignment expression SEMI_COLON interface_next')
        @self.pg.production('actor_next :      VAR WORD COLON datatype Assignment expression SEMI_COLON actor_next')
        @self.pg.production('effect_next :     VAR WORD COLON datatype Assignment expression SEMI_COLON effect_next')
        @self.pg.production('union_start :     VAR WORD COLON datatype Assignment expression SEMI_COLON union_start')
        def var_datatype_Assignment (p):
            pass
        @self.pg.production('struct_next :     STATIC OPTIMISE WORD COLON datatype OPEN_CURLY optimise_start SEMI_COLON')
        @self.pg.production('interface_next :  STATIC OPTIMISE WORD COLON datatype OPEN_CURLY optimise_start SEMI_COLON')
        @self.pg.production('actor_next :      STATIC OPTIMISE WORD COLON datatype OPEN_CURLY optimise_start SEMI_COLON')
        @self.pg.production('effect_next :     STATIC OPTIMISE WORD COLON datatype OPEN_CURLY optimise_start SEMI_COLON')
        @self.pg.production('union_start :     STATIC OPTIMISE WORD COLON datatype OPEN_CURLY optimise_start SEMI_COLON')
        def STATIC_OPTIMISE (p):
            pass
        @self.pg.production('struct_next :     STATIC OPTIMISE LESS WORD GREATER WORD COLON datatype SEMI_COLON optimise_start SEMI_COLON')
        @self.pg.production('interface_next :  STATIC OPTIMISE LESS WORD GREATER WORD COLON datatype SEMI_COLON optimise_start SEMI_COLON')
        @self.pg.production('actor_next :      STATIC OPTIMISE LESS WORD GREATER WORD COLON datatype SEMI_COLON optimise_start SEMI_COLON')
        @self.pg.production('effect_next :     STATIC OPTIMISE LESS WORD GREATER WORD COLON datatype SEMI_COLON optimise_start SEMI_COLON')
        @self.pg.production('union_start :     STATIC OPTIMISE LESS WORD GREATER WORD COLON datatype SEMI_COLON optimise_start SEMI_COLON')
        def STATIC_OPTIMISE (p):
            pass
        @self.pg.production('struct_next :     STATIC OPTIMISE LESS WORD GREATER WORD COLON datatype OPEN_CURLY optimise_start')
        @self.pg.production('interface_next :  STATIC OPTIMISE LESS WORD GREATER WORD COLON datatype OPEN_CURLY optimise_start')
        @self.pg.production('actor_next :      STATIC OPTIMISE LESS WORD GREATER WORD COLON datatype OPEN_CURLY optimise_start')
        @self.pg.production('effect_next :     STATIC OPTIMISE LESS WORD GREATER WORD COLON datatype OPEN_CURLY optimise_start')
        @self.pg.production('union_start :     STATIC OPTIMISE LESS WORD GREATER WORD COLON datatype OPEN_CURLY optimise_start')
        def STATIC_OPTIMISE (p):
            pass
        @self.pg.production('struct_next :     STATIC OPTIMISE LESS WORD GREATER OPEN_CURLY  optimise_start')
        @self.pg.production('interface_next :  STATIC OPTIMISE LESS WORD GREATER OPEN_CURLY  optimise_start')
        @self.pg.production('actor_next :      STATIC OPTIMISE LESS WORD GREATER OPEN_CURLY  optimise_start')
        @self.pg.production('effect_next :     STATIC OPTIMISE LESS WORD GREATER OPEN_CURLY  optimise_start')
        @self.pg.production('union_start :     STATIC OPTIMISE LESS WORD GREATER OPEN_CURLY  optimise_start')
        def STATIC_OPTIMISE_strategy (p):
            pass
        @self.pg.production('struct_next :     datatype WORD OPEN_PAREN  optimise_paren_type_end')
        @self.pg.production('interface_next :  datatype WORD OPEN_PAREN  optimise_paren_type_end')
        @self.pg.production('actor_next :      datatype WORD OPEN_PAREN  optimise_paren_type_end')
        @self.pg.production('effect_next :     datatype WORD OPEN_PAREN  optimise_paren_type_end')
        @self.pg.production('interface_next :  datatype WORD OPEN_PAREN  optimise_paren_type_end')
        def STATIC_OPTIMISE (p):
            pass
        @self.pg.production('interface_next :  datatype WORD OPEN_PAREN optimise_paren_type_end')
        def STATIC_OPTIMISE (p):
            pass
        @self.pg.production('interface_next :  datatype WORD OPEN_PAREN optimise_paren_type_end')
        def STATIC_OPTIMISE (p):
            pass
        @self.pg.production('optimise_paren_type:  LET WORD optimise_paren_type_end')
        @self.pg.production('optimise_paren_type :  VAL WORD optimise_paren_type_end')
        def STATIC_OPTIMISE (p):
            pass
        @self.pg.production('optimise_paren_type:  LET WORD Assignment optimise_paren_type_end')
        @self.pg.production('optimise_paren_type :  VAL WORD Assignment optimise_paren_type_end')
        def STATIC_OPTIMISE (p):
            pass
        @self.pg.production('optimise_paren_type :  LET datatype WORD optimise_paren_type_end')
        @self.pg.production('optimise_paren_type :  VAL datatype WORD optimise_paren_type_end')
        def STATIC_OPTIMISE (p):
            pass
        @self.pg.production('optimise_paren_type :  LET datatype WORD Assignment optimise_paren_type_end')
        @self.pg.production('optimise_paren_type :  VAL datatype WORD Assignment  optimise_paren_type_end')
        def STATIC_OPTIMISE (p):
            pass
        @self.pg.production('optimise_paren_type_end :  optimise_paren_type COMMAR ')
        @self.pg.production('optimise_paren_type_end :   CLOSE_PAREN')
        def STATIC_OPTIMISE (p):
            pass
        @self.pg.production('interface_next :STATIC OPTIMISE LESS WORD GREATER datatype WORD OPEN_PAREN CLOSE_PAREN')
        def STATIC_OPTIMISE_strategy (p):
            pass
        @self.pg.production('interface_next : OPTIMISE datatype WORD OPEN_PAREN CLOSE_PAREN')
        def OPTIMISE_datatype (p):
            pass
        @self.pg.production('interface_next : STATIC OPTIMISE LESS WORD GREATER datatype WORD OPEN_PAREN CLOSE_PAREN')
        def OPTIMISE_datatype (p):
            pass
        @self.pg.production('code : WORD Assignment_ADD  expression  SEMI_COLON code')
        @self.pg.production('code : WORD Assignment_MULT  expression  SEMI_COLON code')
        @self.pg.production('code : WORD Assignment_SUB  expression  SEMI_COLON code')
        @self.pg.production('code : WORD Assignment_XOR  expression  SEMI_COLON code')
        @self.pg.production('code : WORD Assignment_OR  expression  SEMI_COLON code')
        @self.pg.production('code : WORD Assignment_POWER  expression  SEMI_COLON code')
        @self.pg.production('code : WORD Assignment_Not  expression  SEMI_COLON code')
        @self.pg.production('code : WORD Assignment_AND  expression  SEMI_COLON code')
        @self.pg.production('code : WORD Assignment  expression  SEMI_COLON code')
        def expression_end (p):
            inside = p[1]#
            if inside.gettokentype() == 'Assignment_ADD':
                return Assignment_ADD(p[0],p[2],p[4])
            if inside.gettokentype() == 'Assignment_MULT':
                return Assignment_MULT(p[0],p[2],p[4])
            if inside.gettokentype() == 'Assignment_SUB':
                return Assignment_SUB(p[0],p[2],p[4])
            if inside.gettokentype() == 'Assignment_XOR':
                return Assignment_XOR(p[0],p[2],p[4])
            if inside.gettokentype() == 'Assignment_OR':
                return Assignment_OR(p[0],p[2],p[4])
            if inside.gettokentype() == 'Assignment_POWER':
                return Assignment_POWER(p[0],p[2],p[4])
            if inside.gettokentype() == 'Assignment_Not':
                return Assignment_Not(p[0],p[2],p[4])
            if inside.gettokentype() == 'Assignment_AND':
                return Assignment_AND(p[0],p[2],p[4])
            if inside.gettokentype() == 'Assignment':
                return Assignment(p[0],p[2],p[4])


        
        @self.pg.production('code : DELETE WORD')
        def expression_end (p):
            inside = p[1]#
            return DELETE(inside)


        
        @self.pg.production('code : DELETE WORD')
        def expression_end (p):
            inside = p[1]#
            return DELETE(inside)
        
        @self.pg.production('code : SIZEOF WORD')
        def expression_end (p):
            inside = p[1]#
            return SIZEOF(inside)

        @self.pg.production('code : TRY OPEN_CURLY code SEMI_COLON  code')
        def expression_end (p):
            inside = p[2]
            code = p[3]

        @self.pg.production('code : RETURN expression SEMI_COLON  code')
        def expression_end (p):
            inside = p[1]
            code = p[3]
            return RETURN(inside,code)
        @self.pg.production('code : YIELD expression  SEMI_COLON code')
        def expression_end (p):
            inside = p[1]
            code = p[3]
            return YIELD(inside,code)
        @self.pg.production('code : IF OPEN_PAREN expression CLOSE_PAREN   code ifs ')
        def expression_end (p):
            inside = p[3]#
            code = p[5]#
            ifs = p[6]#
            return IF(inside,code,ifs)
        @self.pg.production('ifs : ELSE code')
        def expression_end (p):
            inside = p[1]#
            return ELSE(inside)
        @self.pg.production('ifs : ELSE IF OPEN_PAREN expression CLOSE_PAREN code ifs')
        def ELSE_IF (p):
            inside = p[3]#
            code = p[5]#
            ifs = p[6]#
            return ELSE_IF(inside,code,ifs)
        @self.pg.production('ifs : FOR OPEN_PAREN expression IN expression CLOSE_PAREN code ifs')
        def for_IN (p):
            return ELSE_FOR_IN(p[2],p[4],p[6],p[7])
        
        @self.pg.production('ifs : code ')
        def ELSE_FOR (p):
            inside = p[0]#
            return END_IF(code)
        @self.pg.production('code : FOR OPEN_PAREN expression COMMAR expression COMMAR expression CLOSE_PAREN OPEN_CURLY code code')
        def for_ (p):
            return FOR(p[2],p[4],p[6],p[8],p[9])
        @self.pg.production('code : FOR OPEN_PAREN expression COMMAR expression COMMAR expression CLOSE_PAREN  OPEN_CURLY code code')
        def for_ (p):
            return FOR(p[2],p[4],p[6],p[8],p[9])
        @self.pg.production('code : TRY code')
        @self.pg.production('code : CATCH OPEN_PAREN WORD CLOSE_PAREN OPEN_CURLY code')
        def TRY (p):
            if inside.gettokentype() == 'TRY':
                return TRY(p[1])
            if inside.gettokentype() == 'CATCH':
                return CATCH(p[2],p[4])

        @self.pg.production('actor_next : CLOSE_CURLY')
        @self.pg.production('class_next : CLOSE_CURLY')
        @self.pg.production('struct_next : CLOSE_CURLY')# optimise_start
        @self.pg.production('effect_next : CLOSE_CURLY')
        @self.pg.production('optimise_start : CLOSE_CURLY')
        @self.pg.production('switch_case :  CLOSE_CURLY')
        def directive_end (p):
            print("end")
            return END()
        @self.pg.production('code : CLOSE_CURLY')
        def directive_end (p):
            print("end")
            return END()
        @self.pg.production('code : SWITCH OPEN_PAREN expression CLOSE_PAREN switch_case ')
        def directive_end (p):
            print("end")
            return SWITCH()
        @self.pg.production('switch_case :  CASE expression COLON code switch_case')
        def directive_end (p):
            return CASE()
        @self.pg.production('switch_case :  DEFAULT  COLON code switch_case')
        def directive_end (p):
            return DEFAULT()
        @self.pg.production('switch_case :  BREAK  SEMI_COLON  switch_case')
        def directive_end (p):
            return BREAK()

        @self.pg.production('code : WORD Assignment capabilities datatype STATIC_CAST expression')
        @self.pg.production('code : WORD Assignment capabilities datatype REINTERPRET_CAST expression')
        @self.pg.production('code : WORD Assignment capabilities datatype DYNAMIC_CAST expression')
        @self.pg.production('code : WORD Assignment capabilities datatype CONST_CAST expression')
        @self.pg.production('code : WORD Assignment capabilities datatype CONSUME expression')
        def expression_end (p):
            inside = p[4]
            if inside.gettokentype() == 'STATIC_CAST':
                return STATIC_CAST(p[0],p[2],p[3],p[5])
            if inside.gettokentype() == 'REINTERPRET_CAST':
                return REINTERPRET_CAST(p[0],p[2],p[3],p[5])
            if inside.gettokentype() == 'DYNAMIC_CAST':
                return DYNAMIC_CAST(p[0],p[2],p[3],p[5])
            if inside.gettokentype() == 'CONST_CAST':
                return CONST_CAST(p[0],p[2],p[3],p[5])
            if inside.gettokentype() == 'CONSUME':
                pass

        @self.pg.production('expression : obj_name')
        @self.pg.production('expression : THIS')
        @self.pg.production('expression : ME')
        @self.pg.production('expression : NUMBER_INT')
        @self.pg.production('expression : NUMBER_FLOAT')
        @self.pg.production('expression : FRACTION')
        @self.pg.production('expression : literal_string')
        @self.pg.production('expression : literal_string_empty')
        @self.pg.production('expression : TRUE')
        @self.pg.production('expression : FALSE')
        @self.pg.production('expression : NAME')
        def expression_end (p):
            inside = p[0]
            if inside.gettokentype() == 'NUMBER_INT':
                return NUMBER_INT(inside)
            if inside.gettokentype() == 'NUMBER_FLOAT':
                return NUMBER_FLOAT(inside)   
            if inside.gettokentype() == 'FRACTION':
                return FRACTION(inside) 
            if inside.gettokentype() == 'literal_string':
                return literal_string("") 
            if inside.gettokentype() == 'literal_string_empty':
                return literal_string("") 
            if inside.gettokentype() == 'TRUE':
                return TRUE(inside)  
            if inside.gettokentype() == 'FALSE':
                return FALSE(inside)  
            if inside.gettokentype() == 'NAME':
                return NAME(inside)  
            if inside.gettokentype() == 'obj_name':
                return OBJ_NAME(inside) 
            if inside.gettokentype() == 'THIS':
                return THIS(inside)  
            if inside.gettokentype() == 'ME':
                return ME(inside) 
        
        @self.pg.production('complex : GET WORD OPEN_CURLY code complex')
        @self.pg.production('complex : GET WORD OPEN_CURLY code complex')
        @self.pg.production('complex : GET WORD OPEN_CURLY code complex')
        @self.pg.production('complex : GET OPEN_CURLY code  complex')
        @self.pg.production('complex : SET WORD OPEN_CURLY code complex')
        @self.pg.production('complex : SET WORD OPEN_CURLY code complex')
        @self.pg.production('complex : SET WORD OPEN_CURLY code complex')
        @self.pg.production('complex : SET OPEN_CURLY code  complex')
        def expression_end (p):
            inside = p[0]
            code = p[2]
            complex = p[3]
            if inside.gettokentype() == 'SET':
                return SET(inside,code,complex)
            if inside.gettokentype() == 'GET':
                return GET(inside,code,complex)
        
        @self.pg.production('expression : expression MULT expression')
        @self.pg.production('expression : expression POWER expression')
        @self.pg.production('expression : expression DIV_FLOOR expression')
        @self.pg.production('expression : expression DIV expression')
        @self.pg.production('expression : expression DIV_FLOOR expression')
        @self.pg.production('expression : expression PERCENTAGE expression')
        @self.pg.production('expression : expression HAT expression')
        @self.pg.production('expression : expression AND expression')
        @self.pg.production('expression : expression NOT_EQUAL expression')
        @self.pg.production('expression : expression GREATER_EQUAL expression')
        @self.pg.production('expression : expression LESS_EQUAL expression')
        @self.pg.production('expression : expression PUSH_LEFT expression')
        @self.pg.production('expression : expression PUSH_RIGHT expression')
        @self.pg.production('expression : expression HORIZONTAL_BAR expression')
        @self.pg.production('expression : expression LESS expression')
        @self.pg.production('expression : expression GREATER expression')
        @self.pg.production('expression : expression ADD_UNSAFE expression')
        @self.pg.production('expression : expression SUB_UNSAFE expression')
        @self.pg.production('expression : expression MUL_UNSAFE expression')
        @self.pg.production('expression : expression DIV_UNSAFE expression')
        @self.pg.production('expression : expression REM_UNSAFE expression')
        @self.pg.production('expression : expression MOD_UNSAFE expression')
        @self.pg.production('expression : expression NEG_UNSAFE expression')
        @self.pg.production('expression : expression EQ_UNSAFE expression')
        @self.pg.production('expression : expression NE_UNSAFE expression')
        @self.pg.production('expression : expression LT_UNSAFE expression')
        @self.pg.production('expression : expression GT_UNSAFE expression')
        @self.pg.production('expression : expression LE_UNSAFE expression')
        @self.pg.production('expression : expression GE_UNSAFE expression')
        @self.pg.production('expression : expression ADD_PARTIAL expression')
        @self.pg.production('expression : expression SUB_PARTIAL expression')
        @self.pg.production('expression : expression MUL_PARTIAL expression')
        @self.pg.production('expression : expression DIV_PARTIAL expression')
        @self.pg.production('expression : expression REM_PARTIAL expression')
        @self.pg.production('expression : expression MOD_PARTIAL expression')
        def expression_end (p):
            inside = p[1]
            left = p[0]
            rigth = p[2]
            if inside.gettokentype() == 'MULT':
                return MULT(left,rigth)
            if inside.gettokentype() == 'POWER':
                return POWER(left,rigth)
            if inside.gettokentype() == 'DIV':
                return DIV(left,rigth)
            if inside.gettokentype() == 'DIV_FLOOR':
                return DIV_FLOOR(left,rigth)
            if inside.gettokentype() == 'HAT':
                return HAT(left,rigth)
            if inside.gettokentype() == 'AND':
                return AND(left,rigth)
            if inside.gettokentype() == 'NOT_EQUAL':
                return NOT_EQUAL(left,rigth)
            if inside.gettokentype() == 'GREATER_EQUAL':
                return GREATER_EQUAL(left,rigth)
            if inside.gettokentype() == 'LESS_EQUAL':
                return LESS_EQUAL(left,rigth)
            if inside.gettokentype() == 'PUSH_LEFT':
                return PUSH_LEFT(left,rigth)
            if inside.gettokentype() == 'PUSH_RIGHT':
                return PUSH_RIGHT(left,rigth)
            if inside.gettokentype() == 'LESS':
                return LESS(left,rigth)
            if inside.gettokentype() == 'GREATER':
                return GREATER(left,rigth)
            if inside.gettokentype() == 'ADD_UNSAFE':
                return ADD_UNSAFE(left,rigth)
            if inside.gettokentype() == 'SUB_UNSAFE':
                return SUB_UNSAFE(left,rigth)
            if inside.gettokentype() == 'MUL_UNSAFE':
                return MUL_UNSAFE(left,rigth)
            if inside.gettokentype() == 'DIV_UNSAFE':
                return DIV_UNSAFE(left,rigth)
            if inside.gettokentype() == 'REM_UNSAFE':
                return REM_UNSAFE(left,rigth)
            if inside.gettokentype() == 'MOD_UNSAFE':
                return MOD_UNSAFE(left,rigth)
            if inside.gettokentype() == 'NEG_UNSAFE':
                return NEG_UNSAFE(left,rigth)
            if inside.gettokentype() == 'LT_UNSAFE':
                return LT_UNSAFE(left,rigth)
            if inside.gettokentype() == 'GT_UNSAFE':
                return GT_UNSAFE(left,rigth)
            if inside.gettokentype() == 'LE_UNSAFE':
                return LE_UNSAFE(left,rigth)
            if inside.gettokentype() == 'GE_UNSAFE':
                return GE_UNSAFE(left,rigth)
            if inside.gettokentype() == 'EQ_UNSAFE':
                return EQ_UNSAFE(left,rigth)
            if inside.gettokentype() == 'NE_UNSAFE':
                return NE_UNSAFE(left,rigth)
            if inside.gettokentype() == 'ADD_PARTIAL':
                return ADD_PARTIAL(left,rigth)
            if inside.gettokentype() == 'SUB_PARTIAL':
                return SUB_PARTIAL(left,rigth)
            if inside.gettokentype() == 'MUL_PARTIAL':
                return MUL_PARTIAL(left,rigth)
            if inside.gettokentype() == 'DIV_PARTIAL':
                return DIV_PARTIAL(left,rigth)
            if inside.gettokentype() == 'REM_PARTIAL':
                return REM_PARTIAL(left,rigth)
            if inside.gettokentype() == 'MOD_PARTIAL': # DIV_FLOOR
                return MOD_PARTIAL(left,rigth)
            if inside.gettokentype() == 'DIV_FLOOR': 
                return DIV_FLOOR(left,rigth)
        @self.pg.production('expression : expression INCREMENT')
        @self.pg.production('expression : expression DECREMENT')
        def expression_end (p):
            inside = p[1]
            left = p[0]
            if inside.gettokentype() == 'INCREMENT':
                INCREMENT(left)
            if inside.gettokentype() == 'DECREMENT':
                DECREMENT(left)

        @self.pg.error
        def error_handle(token):
            print(token)
            raise ValueError(token)
    def get_parser(self):
        return self.pg.build()


