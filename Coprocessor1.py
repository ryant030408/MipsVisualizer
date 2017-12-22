class Coprocessor1:

    def __init__(self, number):
        #
        # coprocessor 1
        #

        # floating point return values
        if (number in range(0, 4)):
            self.register_name = '$f' + str(number)
        # temporary registers, not preserved by subprograms
        elif(number in range(4, 11)):
            self.register_name = '$f' + str(number)
        # first two arguments to subprograms, not preserved by subprograms
        elif(number in range(12, 15)):
            self.register_name = '$f' + str(number)
        # more temporary registers, not preserved by subprograms
        elif(number in range(16, 19)):
            self.register_name = '$f' + str(number)
        # saved registers, preserved by subprograms
        elif(number in range(20, 32)):
            self.register_name = '$f' + str(number)