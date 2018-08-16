from ArithmeticLogic import add


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

        self.signed = True if self.bits[0] else False

        def __twos_complement_add(bit_pattern):

            ONE_AS_BIT_PATTERN = [0, 0, 0, 0, 0, 0, 0, 1]

            new_bits = [0] * 8

            for index, digit in enumerate(bit_pattern):
                if digit == 0:
                    new_bits[index] = 1
                else:
                    new_bits[index] = 0

            new_bits_add_one = add(new_bits, ONE_AS_BIT_PATTERN, bit_pattern=True)
            return new_bits_add_one

        self.twos_comp = __twos_complement_add(self.bits)

    def __str__(self):

        return "".join([f"{str(key)}: {str(value)}\n" for key, value in self.__dict__.items()])




