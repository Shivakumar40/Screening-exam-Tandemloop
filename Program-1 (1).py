

class Calculator:

    def __init__(self,a,b,operand) -> None:
        if operand =='+':
            return a+b
        elif operand=='-':
            return a-b
        elif operand=='/':
            return a/b
        else:
            return a*b
