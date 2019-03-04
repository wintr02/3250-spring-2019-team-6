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

