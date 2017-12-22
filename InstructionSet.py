# add registers
def add(dest, first_r, second_r):
    dest.set_value(first_r.value + second_r.value)

# add imediate
def addi(dest, first_r, imm_val):
    dest.set_value(first_r.value + imm_val)

# add immediate unsigned
# TODO implement signed/unsigned
def addiu(dest, first_r, imm_val):
    dest.set_value(first_r.value + imm_val)

# add unisgned
# TODO implement signed/unsigned
def addu(dest, first_r, second_r):
    dest.set_value(first_r.value + second_r.value)

# and registers
def and_r(dest, first_r, second_r):
    dest.set_value(first_r.value & second_r.value)

# and immediate
def andi(dest, first_r, imm_val):
    dest.set_value(first_r.value & imm_val)

# TODO add branch operation


# divide registers
# TODO add overflow
def div(hi_r, lo_r, first_r, second_r):
    lo_r.set_value(first_r.value / second_r.value)

# divide registers unsigned
# TODO add overflow and fix unsigned
def divu(hi_r, lo_r, first_r, second_r):
    lo_r.set_value(first_r.value / second_r.value)

# TODO add jump registers
# TODO add load registers

# move from hi
def mfhi(hi_r, dest):
    dest.set_value(hi_r.value)

# move from lo
def mflo(lo_r, dest):
    dest.set_value(lo_r.value)

# move to hi
def mthi(hi_r, first_r):
    hi_r.set_value(first_r.value)

# move to lo
def mtlo(lo_r, first_r):
    lo_r.set_value(first_r.value)

# multiply registers
# TODO add overflow
def mult(hi_r, lo_r, first_r, second_r):
    lo_r.set_value(first_r.value * second_r.value)

# multiply unsigned registers
# TODO add overflow and fix unsigned
def multu(hi_r, lo_r, first_r, second_r):
    lo_r.set_value(first_r.value * second_r.value)

# nor register
def nor(dest, first_r, second_r):
    dest.set_value(~(first_r.value | second_r.value))

# or registers
def or_r(dest, first_r, second_r):
    dest.set_value(first_r | second_r)

# or immediate
def ori(dest, first_r, imm_val):
    dest.set_value(first_r.value | imm_val)

# TODO rest of instructions, start with store byte