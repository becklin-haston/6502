from ArithmeticLogic import get_2c_bits, get_2c_value


class ByteInteger:

    def __init__(self, value):

        self.dec_value = value
        self.hex_value = hex(value)[2:]
        self.bits = [int(digit) for digit in bin(value)[2:]]
        if len(self.bits) < 8:

            remainder = 8 - len(self.bits)
            remainder_digits = remainder * [0]
            new_bits = remainder_digits + self.bits
            self.bits = new_bits

        #If you're going to store the value, you might well store the bits.

        self.twos_comp_bits = get_2c_bits(self.bits)
        self.twos_comp_value = get_2c_value(self.twos_comp_bits)

        self.signed = True if self.bits[0] else False

    def __str__(self):

        return "ByteInteger " + ", ".join([f"{str(key)}: {str(value)}"\
              for key, value in self.__dict__.items()])


