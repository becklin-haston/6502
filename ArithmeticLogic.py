def create_empty_byte():
    return [0] * 8

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


def boolean_op(operation, **kwargs):

    truth_tables = {
        "AND": {
            (1, 1): 1,
            (1, 0): 0,
            (0, 1): 0,
            (0, 0): 0
        },
        "OR": {
            (1, 1): 1,
            (1, 0): 1,
            (0, 1): 1,
            (0, 0): 0
        },
        "NOT": {
            1: 0,
            0: 1
        }
    }

    current_operation_truth_table = truth_tables[operation]
    new_bits = create_empty_byte()

    if operation != "NOT":
        a = kwargs["a"]
        b = kwargs["b"]
        for i in range(8):
            bit_a = a[i]
            bit_b = b[i]
            new_bits[i] = current_operation_truth_table[(bit_a, bit_b)]

    else:
        a = kwargs["a"]
        for i in range(8):
            bit = a[i]
            new_bits[i] = current_operation_truth_table[bit]

    return new_bits


def AND(a, b):

    return boolean_op("AND", a=a, b=b)


def OR(a, b):

    return boolean_op("OR", a=a, b=b)

#
# def XOR(a, b):
#
#     # (A and NOT B) or NOT A and B
#
#     not_b = NOT(b)
