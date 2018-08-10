class ByteInteger:

    def __init__(self, value, byte_length=8, signed=False):
        if value > 255:
            raise ValueError
        self.signed = signed # TODO implement signed integers
        self.byte_length = byte_length
        self.value = value
        self.bits = [int(digit) for digit in str(bin(value))[2:]]
        self.hex = hex(value)[2:]
        if len(self.bits) < self.byte_length:
            remainder = self.byte_length - len(self.bits)
            remainder_digits = remainder * [0]
            new_bits = remainder_digits + self.bits
            self.bits = new_bits

    def __str__(self):

        return f"bin: {self.bits}, dec: {self.value}, hex: {self.hex}"

    def __add__(self, other):

        new_bits = [0] * 8
        self.bits.reverse()
        other.bits.reverse()
        carry = 0

        for index in range(self.byte_length):
            self_digit = self.bits[index]
            other_digit = other.bits[index]
            current_eval = carry + self_digit + other_digit
            if current_eval == 0:
                new_bits[index] = 0
            elif current_eval == 1:
                if carry:
                    carry = 0
                new_bits[index] = 1
            elif current_eval == 2:
                new_bits[index] = 0
                carry = 1
            elif current_eval == 3:
                new_bits[index] = 1

        try:
            new_bits[index + 1] = carry
        except IndexError:
            pass

        new_bits.reverse()

        str_bits = [str(digit) if digit else "0" for digit in new_bits]
        str_bits = [str(carry)] + str_bits
        new_int = int("".join(str_bits), 2)
        self.bits.reverse()
        other.bits.reverse()
        result = ByteInteger(new_int)
        return result



