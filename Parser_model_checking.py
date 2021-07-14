from rply import ParserGenerator
from ast import  *
class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            [
                'OPEN_PAREN'  ,
                'CLOSE_PAREN' ,
                'OPEN_CURLY'  ,
                'CLOSE_CURLY' ,
                'OPEN_SQUARE' ,
                'CLOSE_SQUARE',
                'STRUCT',
                'CLASS' ,
                'ACTOR' ,
                'EFFECT',
                'ENUM'  ,
            ])
        @self.pg.production('program : complex program')
        def program (p):
            pass
        @self.pg.production('program : STRUCT NAME OPEN_CURLY')
        @self.pg.production('program : CLASS NAME OPEN_CURLY')
        @self.pg.production('program : ACTOR NAME OPEN_CURLY')
        @self.pg.production('program : EFFECT NAME OPEN_CURLY')
        def program (p):
            pass
        @self.pg.production('program : datatype NAME OPEN_SQUARE def_parameter ')
        def program (p):
            pass
        @self.pg.production('def_parameter :  datatype NAME')
        def def_parameter (p):
            pass
        @self.pg.production('def_parameter :   CLOSE_SQUARE')
        def def_parameter (p):
            pass
        @self.pg.production('program : datatype NAME OPEN_SQUARE datatype NAME CLOSE_SQUARE')
        def program (p):
            pass
        #
        @self.pg.production('datatype :BOOL')
        @self.pg.production('datatype :INT')
        @self.pg.production('datatype :INT8_T')
        @self.pg.production('datatype :INT16_T' )
        @self.pg.production('datatype :INT32_T' )
        @self.pg.production('datatype :INT64_T' )
        @self.pg.production('datatype :INTN_T'  )
        @self.pg.production('datatype :UINT4_T' )
        @self.pg.production('datatype :UINT8_T' )
        @self.pg.production('datatype :UINT16_T')
        @self.pg.production('datatype :UINT32_T')
        @self.pg.production('datatype :UINT64_T')
        @self.pg.production('datatype :UINTN_T' )
        @self.pg.production('datatype :SHORT'   )
        @self.pg.production('datatype :TYPE_INFO')
        @self.pg.production('datatype :SIGNED'  )
        @self.pg.production('datatype :STRING'  )
        @self.pg.production('datatype :LONG'    )
        @self.pg.production('datatype :INT'     )
        @self.pg.production('datatype :VOID'    )
        @self.pg.production('datatype :WCHAR_T' )
        def datatype (p):
            print("datatype")
            if inside.gettokentype() ==  'BOOL':
                return BOOL()
            if inside.gettokentype() ==  'INT':
                return INT()
            if inside.gettokentype() ==  'INT8_T':
                return INT8_T()
            if inside.gettokentype() ==  'INT16_T':
                return INT16_T()
            if inside.gettokentype() ==  'INT32_T':
                return INT32_T()
            if inside.gettokentype() ==  'INT64_T':
                return INT64_T()
            if inside.gettokentype() ==  'INTN_T' :
                return INTN_T'()
            if inside.gettokentype() ==  'UINT4_T':
                return UINT4_T()
            if inside.gettokentype() ==  'UINT8_T':
                return UINT8_T()
            if inside.gettokentype() ==  'UINT16_T':
                return UINT16_T()
            if inside.gettokentype() ==  'UINT32_T':
                return UINT32_T()
            if inside.gettokentype() ==  'UINT64_T':
                return UINT64_T()
            if inside.gettokentype() ==  'UINTN_T':
                return UINTN_T()
            if inside.gettokentype() ==  'SHORT'  :
                return SHORT ()
            if inside.gettokentype() ==  'TYPE_INFO':
                return TYPE_INF()
            if inside.gettokentype() ==  'SIGNED' :
                return SIGNED()
            if inside.gettokentype() ==  'STRING' :
                return STRING()
            if inside.gettokentype() ==  'LONG'   :
                return LONG  ()
            if inside.gettokentype() ==  'INT'    :
                return INT   ()
            if inside.gettokentype() ==  'VOID'   :
                return VOID  ()
            if inside.gettokentype() ==  'WCHAR_T':
                return WCHAR_T()

        @self.pg.production('datatype : ARRAY datatype')
        @self.pg.production('datatype : LIST datatype')
        @self.pg.production('datatype : REF datatype')
        @self.pg.production('datatype : STACK datatype')
        @self.pg.production('datatype : QUEUE datatype')
        @self.pg.production('datatype : DEQUE datatype')
        @self.pg.production('datatype : RING datatype')
        @self.pg.production('datatype : ALIST datatype')
        @self.pg.production('datatype : SKIP  datatype')
        def abstract_data_type (p):
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
        
        @self.pg.production('datatype : STRUCT  NAME')
        @self.pg.production('datatype : CLASS  NAME')
        @self.pg.production('datatype : ACTOR  NAME')
        @self.pg.production('datatype : EFFECT  NAME')
        @self.pg.production('datatype : ENUM  NAME')
        def abstract_data_type (p):
            print("datatype")
            inside = p[0]
            if inside.gettokentype() == "STRUCT":
                return STRUCT(p[1])
            if inside.gettokentype() == "CLASS":
                return CLASS(p[1])
            if inside.gettokentype() == "ACTOR":
                return ACTOR(p[1])
            if inside.gettokentype() == "EFFECT":
                return EFFECT(p[1])
            if inside.gettokentype() == "ENUM":
                return ENUM(p[1])
        
        @self.pg.production('capabilities : ISO')
        @self.pg.production('capabilities : VAL')
        @self.pg.production('capabilities : REF')
        @self.pg.production('capabilities : TRN')
        @self.pg.production('capabilities : TAG')
        @self.pg.production('capabilities : BOX')
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
        
        @self.pg.production('capabilities_datatype : capabilities datatype')
        def capabilities_datatype (p):
            pass
        @self.pg.production('complex_next : capabilities_datatype WORD  OPEN_CURLY prams complex_next')
        def complex_next (p):
            pass
        @self.pg.production('prams : capabilities_datatype NAME prams')
        def prams (p):
            pass
        @self.pg.production('prams_next : COMMAR capabilities_datatype NAME prams_next')
        def prams_next (p):
            pass
        @self.pg.production('prams_next : CLOSE_PAREN code OPEN_CURLY')
        def prams_next (p):
            pass
        @self.pg.production('code : THROW')
        def THROW (p):
            pass
        @self.pg.production('complex_next : capabilities_datatype WORD SEMI_COLON complex_next')
        def complex_next (p):
            pass
        @self.pg.production('complex_next : CLOSE_CURLY')
        def complex_next (p):
            pass