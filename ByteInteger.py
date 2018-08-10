from ByteIntegerErrors import SignedIntegerTooLargeError, SignedIntegerTooSmallError


class ByteInteger:

    def __init__(self, value, byte_length=8, signed=False):

        BINARY_SEPARATOR = "b"

        if signed:

            if value >= 2 ** (byte_length - 1):  # upper bound of signed n-bit integer.
                raise SignedIntegerTooLargeError(value, signed)

            elif value <= -(2 ** (byte_length - 1)): # lower bound of signed n-bit integer.
                raise SignedIntegerTooSmallError(value, signed)

        else:

            if value >= 2 ** byte_length:
                raise ValueError

            if value < 0:
                raise ValueError

        self.signed = signed
        self.byte_length = byte_length
        self.value = value
        self.bits = [int(digit) for digit in bin(value).split(BINARY_SEPARATOR)[1]]
        self.hex = hex(value)[2:]

        if len(self.bits) < self.byte_length:

            remainder = self.byte_length - len(self.bits)
            remainder_digits = remainder * [0]
            new_bits = remainder_digits + self.bits
            self.bits = new_bits

        if self.signed:

            self.bits[0] = 1

    def __str__(self):

        return f"bin: {self.bits}, dec: {self.value}, hex: {self.hex}, signed: {self.signed}"

    def __add__(self, other):

        if self.signed or other.signed:
            raise ValueError
            # We'll probably need to modify the __add__ method to deal with signed integers.
            # That is to say, we will need to make this __add__ method work for 2's complement addition.

        new_bits = [0] * self.byte_length
        carry = 0

        # Iterating "backwards" because index 0 of a list contains the most significant bit of an integer.
        # We want to iterate, starting from the least significant bit of an integer at index -1
        # (like in standard hand-done arithmetic)
        for index in range(-1, -(self.byte_length) - 1, -1):

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
            new_bits[index - 1] = carry
        except IndexError:
            pass

        str_bits = [str(digit) if digit else "0" for digit in new_bits]
        str_bits = [str(carry)] + str_bits
        new_int = int("".join(str_bits), 2)
        result = ByteInteger(new_int)

        return result



