from ByteIntegerErrors import IntegerError
from ArithmeticLogic import add


class ByteInteger:

    def __init__(self, value):

        # if value > 255:
        #     raise IntegerError(value)

        self.dec_value = value
        self.hex_value = hex(value)[2:]

        self.bits = [int(digit) for digit in bin(value)[2:]]
        if len(self.bits) < 8:

            remainder = 8 - len(self.bits)
            remainder_digits = remainder * [0]
            new_bits = remainder_digits + self.bits
            self.bits = new_bits

        self.signed = True if self.bits[0] else False

        def __twos_complement(bit_pattern):
            new_bits = [0] * 8

            for index, digit in enumerate(bit_pattern):
                if digit == 0:
                    new_bits[index] = 1
                else:
                    new_bits[index] = 0

            return new_bits




    def __str__(self):

        return f"bin: {self.bits}, dec: {self.dec_value}, hex: {self.hex_value}, signed: {self.signed}"




