class STRUCT():
    def __init__(self, name,inside, inherited):
        self.inside = inside
        self.name = name
        self.inherited = inherited


    def eval(self):
        pass

class CLASS():
    def __init__(self,name,inside, inherited):
        self.inside = inside
        self.name = name
        self.inherited = inherited


    def eval(self):
        pass
        
class ACTOR():
    def __init__(self, name,inside, inherited):
        self.inside = inside
        self.name = name
        self.inherited = inherited


    def eval(self):
        pass
        
class EFFECT():
    def __init__(self, name,inside, inherited):
        self.inside = inside
        self.name = name
        self.inherited = inherited

    def eval(self):
        pass
        
class ENUM():
    def __init__(self, name,inside, inherited):
        self.inside = inside
        self.name = name
        self.inherited = inherited

    def eval(self):
        pass
        
class ABSTRACT():
    def __init__(self, name,inside, inherited):
        self.inside = inside
        self.name = name
        self.inherited = inherited
    def eval(self):
        pass
        
class INTERFACE():
    def __init__(self, name,inside, inherited):
        self.inside = inside
        self.name = name
        self.inherited = inherited

    def eval(self):
        pass
class INTERFACE():
    def __init__(self, name,inside, inherited):
        self.inside = inside
        self.name = name
        self.inherited = inherited

    def eval(self):
        pass
class FITNESS():
    def __init__(self, code):
        self.code = code

    def eval(self):
        pass
class BEFORE():
    def __init__(self, code):
        self.code = code

    def eval(self):
        pass
class AFTER():
    def __init__(self, code):
        self.code = code
class TRAIN():
    def __init__(self, code):
        self.code = code

    def eval(self):
        pass
class LIFE():
    def __init__(self, code):
        self.code = code

    def eval(self):
        pass


class PROGRAM():
    def __init__(self, next):
        self.next = next

    def eval(self):
        pass
class PROGRAM_END ():
    def __init__(self) -> None:
        pass
class OPTIMISE ():
    def __init__(self,optimise,capabilities,datatype,optimise_start) -> None:
        self.optimise = optimise
        self.capabilities = capabilities
        self.datatype = datatype
        self.optimise_start = optimise_start
class END():
    def __init__(self):
        pass

    def eval(self):
        pass
        
class CAPABILITIES():
    def __init__(self):
        pass

    def eval(self):
        pass

class ISO():
    def __init__(self) -> None:
        pass
    def eval(self):
        pass
class VAL():
    def __init__(self) -> None:
        pass
    def eval(self):
        pass
class REF():
    def __init__(self) -> None:
        pass
    def eval(self):
        pass
class TRN():
    def __init__(self) -> None:
        pass
    def eval(self):
        pass
class TAG():
    def __init__(self) -> None:
        pass
    def eval(self):
        pass
class BOX():
    def __init__(self) -> None:
        pass
    def eval(self):
        pass

class VOID():
    def __init__(self):
        pass
    def eval(self):
        pass
class CHAR():
    def __init__(self):
        pass
    def eval(self):
        pass
class CHAR8():
    def __init__(self):
        pass
    def eval(self):
        pass
class CHAR16():
    def __init__(self):
        pass
    def eval(self):
        pass
class CHAR32():
    def __init__(self):
        pass
    def eval(self):
        pass
class BOOL():
    def __init__(self):
        pass
    def eval(self):
        pass
class AUTO():
    def __init__(self):
        pass
    def eval(self):
        pass
class INT():
    def __init__(self):
        pass
    def eval(self):
        pass
class LONG():
    def __init__(self):
        pass
    def eval(self):
        pass
class LONG_INT():
    def __init__(self):
        pass
    def eval(self):
        pass
class LONG_LONG():
    def __init__(self):
        pass
    def eval(self):
        pass
class SHORT():
    def __init__(self):
        pass
    def eval(self):
        pass
class FLOAT():
    def __init__(self):
        pass
    def eval(self):
        pass
class DOUBLE():
    def __init__(self):
        pass
    def eval(self):
        pass
class LONG_DOUBLE():
    def __init__(self):
        pass
    def eval(self):
        pass
class UNSIGNED_AUTO():
    def __init__(self):
        pass
    def eval(self):
        pass
class UNSIGNED_INT():
    def __init__(self):
        pass
    def eval(self):
        pass
class UNSIGNED_LONG():
    def __init__(self):
        pass
    def eval(self):
        pass
class UNSIGNED_LONG_INT():
    def __init__(self):
        pass
    def eval(self):
        pass
class UNSIGNED_LONG_LONG():
    def __init__(self):
        pass
    def eval(self):
        pass
class UNSIGNED_SHORT():
    def __init__(self):
        pass
    def eval(self):
        pass
class UNSIGNED_FLOAT():
    def __init__(self):
        pass
    def eval(self):
        pass
class UNSIGNED_DOUBLE():
    def __init__(self):
        pass
    def eval(self):
        pass
class UNSIGNED_LONG_DOUBLE():
    def __init__(self):
        pass
    def eval(self):
        pass
class SIGNED_AUTO():
    def __init__(self):
        pass
    def eval(self):
        pass
class SIGNED_INT():
    def __init__(self):
        pass
    def eval(self):
        pass
class SIGNED_LONG():
    def __init__(self):
        pass
    def eval(self):
        pass
class SIGNED_LONG_INT():
    def __init__(self):
        pass
    def eval(self):
        pass
class SIGNED_LONG_LONG():
    def __init__(self):
        pass
    def eval(self):
        pass
class SIGNED_SHORT():
    def __init__(self):
        pass
    def eval(self):
        pass
class SIGNED_FLOAT():
    def __init__(self):
        pass
    def eval(self):
        pass
class SIGNED_DOUBLE():
    def __init__(self):
        pass
    def eval(self):
        pass
class SIGNED_LONG_DOUBLE():
    def __init__(self):
        pass
    def eval(self):
        pass
class INT8_T():
    def __init__(self):
        pass
    def eval(self):
        pass
class INT16_T():
    def __init__(self):
        pass
    def eval(self):
        pass
class INT32_T():
    def __init__(self):
        pass
    def eval(self):
        pass
class INT64_T():
    def __init__(self):
        pass
    def eval(self):
        pass
class INTN_T():
    def __init__(self):
        pass
    def eval(self):
        pass
class UINT4_T():
    def __init__(self):
        pass
    def eval(self):
        pass
class UINT8_T():
    def __init__(self):
        pass
    def eval(self):
        pass
class UINT16_T():
    def __init__(self):
        pass
    def eval(self):
        pass
class UINT32_T():
    def __init__(self):
        pass
    def eval(self):
        pass
class UINT64_T():
    def __init__(self):
        pass
    def eval(self):
        pass
class UINTN_T():
    def __init__(self):
        pass
    def eval(self):
        pass
class STRING():
    def __init__(self):
        pass
    def eval(self):
        pass
class VOID():
    def __init__(self):
        pass
    def eval(self):
        pass
class WCHAR_T():
    def __init__(self):
        pass
    def eval(self):
        pass

class ADD():
    def __init__(self) -> None:
        pass
class MULT():
    def __init__(self) -> None:
        pass
class SUB():
    def __init__(self) -> None:
        pass
class XOR():
    def __init__(self) -> None:
        pass
class DIV():
    def __init__(self) -> None:
        pass
class DIV_FLOOR():
    def __init__(self) -> None:
        pass
class HAT():
    def __init__(self) -> None:
        pass
class NOT_EQUAL():
    def __init__(self) -> None:
        pass
class GREATER_EQUAL():
    def __init__(self) -> None:
        pass
class PUSH_LEFT():
    def __init__(self) -> None:
        pass
class LESS_EQUAL():
    def __init__(self) -> None:
        pass
class PUSH_RIGHT():
    def __init__(self) -> None:
        pass
class LESS():
    def __init__(self) -> None:
        pass
class ADD_UNSAFE():
    def __init__(self) -> None:
        pass
class SUB_UNSAFE():
    def __init__(self) -> None:
        pass
class MUL_UNSAFE():
    def __init__(self) -> None:
        pass
class DIV_UNSAFE():
    def __init__(self) -> None:
        pass
class REM_UNSAFE():
    def __init__(self) -> None:
        pass
class MOD_UNSAFE():
    def __init__(self) -> None:
        pass
class NEG_UNSAFE():
    def __init__(self) -> None:
        pass
class LT_UNSAFE():
    def __init__(self) -> None:
        pass
class GT_UNSAFE():
    def __init__(self) -> None:
        pass
class LE_UNSAFE():
    def __init__(self) -> None:
        pass
class GE_UNSAFE():
    def __init__(self) -> None:
        pass
class EQ_UNSAFE():
    def __init__(self) -> None:
        pass
class NE_UNSAFE():
    def __init__(self) -> None:
        pass
class ADD_PARTIAL():
    def __init__(self) -> None:
        pass
class SUB_PARTIAL():
    def __init__(self) -> None:
        pass
class MUL_PARTIAL():
    def __init__(self) -> None:
        pass
class DIV_PARTIAL():
    def __init__(self) -> None:
        pass
class REM_PARTIAL():
    def __init__(self) -> None:
        pass
class MOD_PARTIAL():
    def __init__(self) -> None:
        pass

    
class NOT_EQUAL():
    def __init__(self) -> None:
        pass
class OR():
    def __init__(self) -> None:
        pass
class POWER():
    def __init__(self) -> None:
        pass
class Not():
    def __init__(self) -> None:
        pass
class AND():
    def __init__(self) -> None:
        pass
class Assignment():
    def __init__(self) -> None:
        pass
class Variable(): 
    def __init__(self,capabilities,datatype,name,expression =None) -> None:
        self.capabilities =capabilities
        self.datatype =datatype
        self.name =name
        self.expression = expression

class Assignment_ADD():
    def __init__(self) -> None:
        pass

class GREATER():
    def __init__(self) -> None:
        pass
class Assignment_MULT():
    def __init__(self) -> None:
        pass
class Assignment_SUB():
    def __init__(self) -> None:
        pass
class Assignment_XOR():
    def __init__(self) -> None:
        pass
class Assignment_OR():
    def __init__(self) -> None:
        pass
class Assignment_POWER():
    def __init__(self) -> None:
        pass
class Assignment_Not():
    def __init__(self) -> None:
        pass
class Assignment_AND():
    def __init__(self) -> None:
        pass
class Assignment():
    def __init__(self) -> None:
        pass

class RETURN():
    def __init__(self) -> None:
        pass
class YIELD():
    def __init__(self) -> None:
        pass
class IF():
    def __init__(self) -> None:
        pass
class ELSE():
    def __init__(self) -> None:
        pass
class ELSE_IF():
    def __init__(self) -> None:
        pass
class ELSE_FOR():
    def __init__(self) -> None:
        pass
class FOR():
    def __init__(self) -> None:
        pass
class END_IF():
    def __init__(self) -> None:
        pass


class NAME():
    def __init__(self) -> None:
        pass
class FALSE():
    def __init__(self) -> None:
        pass
class TRUE():
    def __init__(self) -> None:
        pass
class literal_string():
    def __init__(self) -> None:
        pass
class FRACTION():
    def __init__(self) -> None:
        pass
class NUMBER_FLOAT():
    def __init__(self) -> None:
        pass
class NUMBER_INT():
    def __init__(self) -> None:
        pass

class DYNAMIC_CAST():
    def __init__(self) -> None:
        pass
class REINTERPRET_CAST():
    def __init__(self) -> None:
        pass
class STATIC_CAST():
    def __init__(self) -> None:
        pass

class LIST():
    def __init__(self) -> None:
        pass
class ARRAY():
    def __init__(self) -> None:
        pass
class SKIP():
    def __init__(self) -> None:
        pass
class RING():
    def __init__(self) -> None:
        pass
class DEQUE():
    def __init__(self) -> None:
        pass
class QUEUE():
    def __init__(self) -> None:
        pass
class STACK():
    def __init__(self) -> None:
        pass
class THROW():
    def __init__(self) -> None:
        pass
class CODE():
    def __init__(self,capabilities, datatype,code,effect_next) -> None:
        pass
class capabilities_datatype():
    def __init__(self,capabilities, datatype) -> None:
        pass

