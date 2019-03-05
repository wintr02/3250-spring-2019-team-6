#Class uses stack operations to do simple integer stacks
class IntegerOpCodes:
    def __init__(self):
        self.stack = []

    #adds top two operands in the stack and returns the value
    def iadd(self):
        self.stack.append(self.stack.pop() + self.stack.pop())

    #Compares top two integer bits in the stack and returns the AND result
    def iand(self):
        self.stack.append(self.stack.pop() & self.stack.pop())

    #Pushes -1 onto the stack
    def iconst_m1(self):
        self.stack.append(-1)

    #Pushes 0 onto the stack
    def iconst_0(self):
        self.stack.append(0)

    #Pushes 1 onto the stack
    def iconst_1(self):
        self.stack.append(1)

    #Pushes 2 onto the stack
    def iconst_2(self):
        self.stack.append(2)

    #Pushes 3 onto the stack
    def iconst_3(self):
        self.stack.append(3)

    #Pushes 4 onto the stack
    def iconst_4(self):
        self.stack.append(4)

    #Pushes 5 onto the stack
    def iconst_5(self):
        self.stack.append(5)

    #Divides top two integers on the stack and pushes the integer answer
    def idiv(self):
        self.stack.append(self.stack.pop()//self.stack.pop())

    #Multiplies top two integers on the stack and pushes the result to the stack
    def imul(self):
        self.stack.append(self.stack.pop()*self.stack.pop())

    #Pushes the next integer on the stack *-1
    def ineg(self):
        self.stack.append(self.stack.pop() * (-1))

    #Pushes bitwise int OR into the stack of the top two integers
    def ior(self):
        self.stack.append(self.stack.pop()|self.stack.pop())

    #Pushes the remainder of the division of the top two integers in the stack
    def irem(self):
        self.stack.append(self.stack.pop()%self.stack.pop())

    #Pushes the next integer on the stack back onto it after it was shifted left by the amount
    #of the the second integer on the stack
    def ishl(self):
        self.stack.append(self.stack.pop()<<self.stack.pop())

    #Pushes the next integer on the stack back onto it after it was arithmetically shifted right by the amount
    #of the the second integer on the stack
    def ishr(self):
        self.stack.append(self.stack.pop()>>self.stack.pop())

    #Pushes the result of the top two integers of the stack back onto the stack
    def isub(self):
        self.stack.append(self.stack.pop()-self.stack.pop())

    #Pushes the next integer on the stack back onto it after it was logically shifted right by the amount
    #of the the second integer on the stack
    def iushr(self):
        self.stack.append((self.stack.pop() % 0x100000000) >> self.stack.pop())#needs testing

    #Pushes the exclusive OR result of the top two integers of the stack back onto the stack
    def ixor(self):
        self.stack.append(self.stack.pop() ^ self.stack.pop())