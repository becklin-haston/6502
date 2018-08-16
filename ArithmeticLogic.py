
def add(first, second, bit_pattern=False):

    if not bit_pattern:
        first = first.bits
        second = second.bits

    START_INDEX = -1
    STOP_INDEX = -9
    LOOP_STEP = -1

    new_bits = [0] * 8
    carry = 0
    for index in range(START_INDEX, STOP_INDEX, LOOP_STEP):

        self_digit = first[index]
        other_digit = second[index]

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

    int_bits = [int(digit) for digit in new_bits]
    if bit_pattern:
        return int_bits
    else:
        str_bits = [str(digit) if digit else "0" for digit in new_bits]
        new_int = int("".join(str_bits), 2)
        return new_int


