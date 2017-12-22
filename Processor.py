import Register
class Processor:
    def __init__(self):
        self.registers = []
        for i in range(0, 32):
            self.registers.append(Register.Register(i))
