import Register, InstructionSet

a = Register.Register(8)
b = Register.Register(9)
c = Register.Register(10)
a.set_value(32)
b.set_value(40)
InstructionSet.add(c, a, b)
print(c.value)