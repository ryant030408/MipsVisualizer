import numpy as np

class Register:

    def __init__(self, number):
        self.value = np.int32(0)

        #
        # standard registers
        #

        # 0 register
        if(number == 0):
            self.register_name = '$0'
        # for pseudo-instructions
        elif(number == 1):
            self.register_name = '$1' # or $at
        # returns values from functions
        elif(number in range(2, 4)):
            self.register_name = '$v' + str(number-2)
        # arguments to functions
        elif(number in range(4,  8)):
            self.register_name = '$a' + str(number-4)
        # temporary registers, not preserved by subprograms
        elif(number in range(8, 16)):
            self.register_name = '$t' + str(number - 8)
        # saved registers, preserved by subprograms
        elif (number in range(16, 24)):
            self.register_name = '$s' + str(number - 16)
        # more temporary registers, not preserved
        elif(number in range(24, 26)):
            self.register_name = '$t' + str(number - 16)
        # reserved for kernal, dont use
        elif(number in range(26, 28)):
            self.register_name = '$k' + str(number - 26)
        # global area pointer
        elif(number == 28):
            self.register_name = '$gp'
        # stack pointer
        elif(number == 29):
            self.register_name = '$sp'
        # frame pointer
        elif(number == 30):
            self.register_name = '$fp'
        # return address
        elif(number == 31):
            self.register_name = '$ra'
        # hi register
        # TODO make lo overflow to hi
        elif(number == 32):
            self.register_name = 'HI'
        # lo register
        elif(number == 33):
            self.register_name = 'LO'
    # set register value
    def set_value(self, value):
        self.value = value