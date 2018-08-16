from ArithmeticLogic import add


class ByteInteger:

    def __init__(self, value):

        def get_twos_comp_value(bit_pattern):

            ONE_AS_BIT_PATTERN = [0, 0, 0, 0, 0, 0, 0, 1]

            def invert_bits(bits):
                new_bit_pattern = [0] * 8
                for index, bit in enumerate(bits):
                    if bit == 0:
                        new_bit_pattern[index] = 1
                    else:
                        new_bit_pattern[index] = 0

                return new_bit_pattern

            sign_bit = bit_pattern[0]
            inverted_bits = invert_bits(bit_pattern)
            twos_comp_bit_pattern = add(inverted_bits, ONE_AS_BIT_PATTERN, bit_pattern=True)
            str_bits = [str(digit) for digit in twos_comp_bit_pattern]
            new_int = int("".join(str_bits), 2)

            return -new_int if sign_bit else new_int


        self.dec_value = value
        self.hex_value = hex(value)[2:]

        self.bits = [int(digit) for digit in bin(value)[2:]]
        if len(self.bits) < 8:

            remainder = 8 - len(self.bits)
            remainder_digits = remainder * [0]
            new_bits = remainder_digits + self.bits
            self.bits = new_bits

        self.twos_comp_value = get_twos_comp_value(self.bits)

        self.signed = True if self.bits[0] else False


    def __str__(self):

        return "".join([f"{str(key)}: {str(value)}\n" for key, value in self.__dict__.items()])




