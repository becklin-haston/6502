from NewByteInteger import ByteInteger


def add(first, second):

    new_bits = [0] * 8
    carry = 0

    # Iterating "backwards" because index 0 of a list contains the most significant bit of an integer.
    # We want to iterate, starting from the least significant bit of an integer at index -1
    # (like in standard hand-done arithmetic)
    START_INDEX = -1
    STOP_INDEX = -9
    LOOP_STEP = -1

    for index in range(START_INDEX, STOP_INDEX, LOOP_STEP):

        self_digit = first.bits[index]
        other_digit = second.bits[index]

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
    new_int = int("".join(str_bits), 2)
    result = ByteInteger(new_int)

    return result

