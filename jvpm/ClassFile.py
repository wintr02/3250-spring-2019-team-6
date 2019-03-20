import unittest
import csv
import struct
import array
# unittest

class ClassFile:
    def __init__(self, file='test/JavaTestStuff2.class'):
        with open(file, 'rb') as binary_file:
            # the byte string being stored in self.data to be parsed
            self.data = binary_file.read()
            self.magic = self.get_magic()
            self.minor = self.get_minor()
            self.major = self.get_major()
            self.constant_pool_count = self.get_constant_pool()-1
            self.constant_pool_helper = self.load_constant_helper()
            self.constant_table, self.constant_pool_length =  self.get_constant_pool_table()
            # self.access_flags = self.get_access_flags()
            # self.this_class = self.get_this_class()
            # self.superclass = self.get_super_class()
            # self.interface_count = self.get_interface_count()
            # self.cp_and_ic = self.interface_count + self.constant_table['length']
            # self.interface_table = self.get_interface_table()
            # self.field_count = self.get_field_count()
            # self.cp_ic_fc = 224 #  = self.cp_and_ic + self.field_count
            # self.field_table = self.get_field_table()
            # self.method_count = self.get_method_count()
            # self.method_table = self.get_method_table()
            #self.cp_ic_fc_mc = self.cp_ic_fc + len(self.method_table)
            # self.attribute_count = self.get_attribute_count()
            # self.attribute_table = self.get_attribute_table()

    def load_constant_helper(self):
        dict_variable_length = {}
        with open('jvpm/files/constant_codes.csv', 'r') as csvfile:
            spamreader = csv.DictReader(csvfile)
            for x in list(spamreader):
                constant_info = {}
                constant_info['num_initial_bytes'] = int(x['Additional bytes'].strip())
                constant_info['variable_length']=bool(int(x['Variable Length'].strip()))
                constant_info['description']=x['Description'].strip()
                the_number = int(x['Tag byte'].strip(),10)
                dict_variable_length[the_number]=constant_info
        return dict_variable_length

    def get_magic(self):
        magic = ""
        for i in range(4):
            magic += format(self.data[i], '02X')
        return magic

    def get_minor(self):
        return self.data[4] + self.data[5]

    def get_major(self):
        return self.data[6] + self.data[7]

    def get_constant_pool(self):
        return self.data[8] + self.data[9]

    def get_constant_pool_table(self):
        #constant = self.data[10:(10+self.constant_pool)]
        the_table = {}
        active_position=10
        for i in range(1,self.constant_pool_count+1):
            dict_constant={}
            constant_code=0
            for j in self.data[active_position:active_position+1]:
                constant_code+= j
            #print("Constant code: ", constant_code)
            active_position+=1
            dict_constant['constant_code']=constant_code
            message_length=int(self.constant_pool_helper[constant_code]['num_initial_bytes'])
            dict_constant['message']=self.data[active_position:active_position+message_length]
            active_position+=message_length
            if(self.constant_pool_helper[constant_code]['variable_length']):
                value_length=int(dict_constant['message'][0]) + int(dict_constant['message'][1])
                dict_constant['value']=self.data[active_position:active_position+value_length]
                active_position+=value_length
            #print(dict_constant)
            the_table[i] = dict_constant
        return the_table, (active_position - 10)
    #
    # def get_access_flags(self):
    #     return self.data[10 + self.constant_pool-1:11 + self.constant_pool]
    #
    # def get_this_class(self):
    #     return self.data[12 + self.constant_pool] + self.data[13 + self.constant_pool]
    #
    # def get_super_class(self):
    #     return self.data[14 + self.constant_pool] + self.data[15 + self.constant_pool]
    #
    # def get_interface_count(self):
    #     return self.data[16 + self.constant_pool] + self.data[17 + self.constant_pool]
    #
    # def get_interface_table(self):
    #     interface = ""
    #     for i in range(self.interface_count):
    #         interface += format(self.data[i + 18 + self.constant_pool], '02X')
    #     return interface
    #
    # def get_field_count(self):
    #     return self.data[18 + self.cp_and_ic] + self.data[19 + self.cp_and_ic]
    #
    # def get_field_table(self):
    #     field = self.data[self.cp_and_ic+20:(self.field_count+self.cp_ic_fc+20)]
    #     # for i in range(self.field_count):
    #     #    field += format(self.data[i + 20 + self.cp_and_ic], '02X')
    #     return field

    def get_method_count(self):
        return self.data[20 + self.cp_ic_fc] + self.data[21 + self.cp_ic_fc]

    def get_method_table(self):
        method = self.data[22+self.cp_ic_fc:22+self.cp_ic_fc+self.method_count]
        return method
    #
    # def get_attribute_count(self):
    #     return self.data[22 + self.cp_ic_fc_mc] + self.data[23 + self.cp_ic_fc_mc]
    #
    # def get_attribute_table(self):
    #     attribute = self.data[(24+self.cp_ic_fc_mc):(24+self.cp_ic_fc_mc+self.attribute_count)]
    #     # for i in range(self.attribute_count):
    #     #    attribute += format(self.data[i + 24 + self.cp_ic_fc_mc], '02X')
    #     return attribute
    #
    def print_self(self):
    #     print(self)
        print("Magic: ", self.magic)
        print("Minor version: ", self.minor)
        print("Major version: ", self.major)
        print("Constant pool count: ", self.constant_pool_count)
    #    print("Constant pool helper: ", self.constant_pool_helper)
        print("Constant pool table: ", self.constant_table)
        print("Constant pool byte length: ", self.constant_pool_length)
    #     print("Access flags: ", hex(self.access_flags[0]), hex(self.access_flags[1]))
    #     print("This class: ", self.this_class)
    #     print("Superclass: ", self.superclass)
    #     print("Interface count: ", self.interface_count)
    #     print("Cp + Ic: ", self.cp_and_ic)
    #     print("Field count: ", self.field_count)
    #     print("Cp + Ic + fc: ", self.cp_ic_fc)
    #     print("Field table: ", "[%s]" % ", ".join(map(str, self.field_table)))
    #    print("Method count: ", self.method_count)
    #     print("Cp + IC + Fc + Mc: ", self.cp_ic_fc_mc)
    #    print("Opcode table: ",''.join("%02x, "%i for i in self.method_table))
    #     print("Attribute count: ", self.attribute_count)
    #     print("Attribute table: ", "[%s]" % ", ".join(map(str, self.attribute_table)))

    def run_opcodes(self):
        opcodes = OpCodes(self.method_table)
        opcodes.run()

#
# if '__main__' == __name__:
#     ClassFile()

'''class LocalVar:
    def __init__(self, localvar=[]):
        self.localvar = localvar
'''

class OpCodes:

    def __init__(self,opcodes=[]):
        self.table = self.load() #{0x00: self.not_implemented} #TODO read in table with opcodes
        self.stack = []
        self.localvar = [0]*10
        self.opcodes = opcodes
        #self.run()

    def load(self):
	    dict1 = {}
	    with open('jvpm/files/int_opcodes.csv', 'r') as csvfile:
		    spamreader = csv.DictReader(csvfile)
		    for x in list(spamreader):
			    the_number = int(x['opcode'].strip(),16)
			    dict1[the_number]=x['name'].strip()
	    return dict1

    def run(self):
        for _ in self.opcodes:
            print("stack: ", self.stack)
            #method = self.interpret(i)
            #print("running method", method, "...")
            #print("finished method", method, "...")
            #test = input()

    def not_implemented(self):
        return 'not implemented'

    def interpret(self, value):
        print("running method: ", self.table[value])
        getattr(self, self.table[value])()
        return self.table[value]

    def push_int_to_stack(self,value):
        if(value>2147483647 or value<-2147483648):
            raise ValueError()
        else:
            self.stack.append(value)

    #adds top two operands in the stack and returns the value
    def iadd(self):
        self.push_int_to_stack(self.stack.pop() + self.stack.pop())

    #Compares top two integer bits in the stack and returns the AND result
    def iand(self):
        self.push_int_to_stack(self.stack.pop() & self.stack.pop())

    #Pushes -1 onto the stack
    def iconst_m1(self):
        self.push_int_to_stack(-1)

    #Pushes 0 onto the stack
    def iconst_0(self):
        self.push_int_to_stack(0)

    #Pushes 1 onto the stack
    def iconst_1(self):
        self.push_int_to_stack(1)

    #Pushes 2 onto the stack
    def iconst_2(self):
        self.push_int_to_stack(2)

    #Pushes 3 onto the stack
    def iconst_3(self):
        self.push_int_to_stack(3)

    #Pushes 4 onto the stack
    def iconst_4(self):
        self.push_int_to_stack(4)

    #Pushes 5 onto the stack
    def iconst_5(self):
        self.push_int_to_stack(5)

    #Divides top two integers on the stack and pushes the integer answer
    def idiv(self):
        self.push_int_to_stack(self.stack.pop()//self.stack.pop())

    #Multiplies top two integers on the stack and pushes the result to the stack
    def imul(self):
        self.push_int_to_stack(self.stack.pop()*self.stack.pop())

    #Pushes the next integer on the stack *-1
    def ineg(self):
        self.push_int_to_stack(self.stack.pop() * (-1))

    #Pushes bitwise int OR into the stack of the top two integers
    def ior(self):
        self.push_int_to_stack(self.stack.pop()|self.stack.pop())

    #Pushes the remainder of the division of the top two integers in the stack
    def irem(self):
        self.push_int_to_stack(self.stack.pop()%self.stack.pop())

    #Pushes the next integer on the stack back onto it after it was shifted left by the amount
    #of the the second integer on the stack
    def ishl(self):
        self.push_int_to_stack(self.stack.pop()<<self.stack.pop())

    #Pushes the next integer on the stack back onto it after it was arithmetically shifted right by the amount
    #of the the second integer on the stack
    def ishr(self):
        self.push_int_to_stack(self.stack.pop()>>self.stack.pop())

    #Pushes the result of the top two integers of the stack back onto the stack
    def isub(self):
        self.push_int_to_stack(self.stack.pop()-self.stack.pop())

    #Pushes the next integer on the stack back onto it after it was logically shifted right by the amount
    #of the the second integer on the stack
    def iushr(self):
        self.push_int_to_stack((self.stack.pop() % 0x100000000) >> self.stack.pop())#needs testing

    #Pushes the exclusive OR result of the top two integers of the stack back onto the stack
    def ixor(self):
        self.push_int_to_stack(self.stack.pop() ^ self.stack.pop())

    #Load specified integer value onto the operand stack
    def iload(self, index):
        self.stack.append(self.localvar[index])

    #Load integer value in localvar list at index 0 to operand stack
    def iload_0(self, index):
        self.stack.append(self.localvar[index])

    #Load integer value in localvar list at index 1 to operand stack
    def iload_1(self, index):
        self.stack.append(self.localvar[index])

    #Load integer value in localvar list at index 2 to operand stack
    def iload_2(self, index):
        self.stack.append(self.localvar[index])

    #Load integer value in localvar list at index 3 to operand stack
    def iload_3(self, index):
        self.stack.append(self.localvar[index])

    #Store specified integer value into localvar list at index 0
    def istore(self, index):
        self.localvar[index] = self.stack.pop()

    #Store integer value on operand stack to localvar list at index 1
    def istore_1(self, index):
        self.localvar[index] = self.stack.pop()

    #Store integer value on operand stack to localvar list at index 2
    def istore_2(self, index):
        self.localvar[index] = self.stack.pop()

    #Store integer value on operand stack to localvar list at index 3
    def istore_3(self, index):
        self.localvar[index] = self.stack.pop()

    def i2b(self):
        self.stack.append(self.stack.pop().to_bytes(length = 1, byteorder = 'big', signed = True))

    def i2c(self):
        #self.stack.append(self.stack.pop().char(c))
        self.stack.append(chr(self.stack.pop()))

    def i2d(self):
        self.stack.append(self.stack.pop()/1.0)

    def i2f(self):
        self.stack.append(self.stack.pop()/1.0)

    def i2l(self):
        max = 2 ** 64 - 1
        min = -2 ** 64
        value = self.stack.pop()
        if value >= min and value <= max:
            self.stack.append(value / 1.0)
        else:
            raise ValueError("Value {} cannot be converted to long".format(value))

    def i2s(self):
        max = 2**16-1
        min = -2**16
        value = self.stack.pop()
        if value >= min and value <= max:
            self.stack.append(value/1.0)
        else:
            raise ValueError("Value {} cannot be converted to short".format(value))


    def invokeVirtual(self, methodRef):
        if (methodRef == "java/io/PrintStream.println:(I)V"):
            return(int(self.stack.pop()))
        #elif (methodRef == "java/util/Stack.push:(Ljava/lang/Object;)Ljava/lang/Object"):
        #   return self.stack.append(self.stack.pop())
        elif (methodRef == "java/io/PrintStream.println:(Z)V"):
            x = self.stack.pop()
            if (x == 1):
                return("true")
            elif (x == 0):
                return("false")
            else:
                return("not a boolean")  # Case probably raises an exception not 'not a boolean' - Christian
        #elif (methodRef == "Method java/io/PrintStream.println:(D)V"):
        #    return(long(self.stack.pop()))
        elif (methodRef == "java/io/PrintStream.println:(Ljava/lang/String;)V"):
            return(self.stack.pop())
        else:
            return("not implemented")
