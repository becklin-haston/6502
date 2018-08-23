
def create_empty_byte():
    return [0] * 8

"""
MANY FUNCTIONS-WHICH-HELP.
"""

def dec_value_from_bits(bits):
    #TURN BITS INTO DECIMAL VALUES WITH THIS ONE GROSS TRICK
    return sum([int(i[1])*(2**(7-i[0])) for i in enumerate(bits)])

def shift_left(bit_pattern):
    #a shimmy-shimmy-shimmy-shimmy-shimmy to the left.
    bit_new = [0]*8
    for i in range(1,8):
        if bit_pattern[i] == 1:
            bit_new[i-1] = 1
    return bit_new

def shift_right(bit_pattern):
    #a shimmy-shimmy-shimmy-shimmy-shimmy to the right.
    bit_new = [0]*8
    for i in range(0,7):
        if bit_pattern[i] == 1:
            bit_new[i+1] = 1
    return bit_new

def shift_left_n(bit_pattern, n):
    #shimmy multiple times to the left
    for i in range(n):
        bit_pattern = shift_left(bit_pattern)
    return bit_pattern

def shift_right_n(bit_pattern, n):
    #shimmy multiple times to the right
    for i in range(n):
        bit_pattern = shift_right(bit_pattern)
    return bit_pattern

"""
ADD IS STRANGE, BECAUSE IT IS TECHNICALLY A FUNCTION-WHICH-HELPS.
"""
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

def get_2c_bits(bit_pattern):
    """
    Returns the 2's complement of the bits.
    """
    ONE_AS_BIT_PATTERN = [0, 0, 0, 0, 0, 0, 0, 1]

    def invert_bits(bits):
        new_bit_pattern = [0] * 8
        for index, bit in enumerate(bits):
            if bit == 0:
                new_bit_pattern[index] = 1
            else:
                new_bit_pattern[index] = 0

        return new_bit_pattern

    inverted_bits = invert_bits(bit_pattern)
    twos_comp_bit_pattern = add(inverted_bits, ONE_AS_BIT_PATTERN, bit_pattern=True)
    
    return twos_comp_bit_pattern 

def get_2c_value(bit_pattern):

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

"""
MANY FUNCTIONS WHICH ARE COMPOSED OF FUNCTIONS WHICH HELP.
"""

def leq(first, second):
    """
    calculates first <= second by direct subtraction.
    
    eg;
    
    [1, 0, 1, 1, 0, 1, 0, 1] <= [1, 1, 0, 1, 1, 0, 0, 0] ?
    
    itemwise subtr:
        [1, 0, 1, 1, 0, 1, 0, 1]
    -   [1, 1, 0, 1, 1, 0, 0, 0]
    _______________________________
        [0,-1, 1, 0,-1, 1, 0, 1]
    
    Go through until you see a -1 or a 1.
    
    If there's a -1, the second is bigger than the first. Return True.
    If there's a 1, the second is smaller than the first. Return False.
    If you hit all zeros, they're the same. Return True,
    """
    compare = [first[i] - second[i] for i in range(8)]
    for i in compare:
        if i > 0:
            return False
        if i < 0:
            return True
    return True


def less_than(first, second):
    #Same as leq, but less forgiving.
    compare = [first[i] - second[i] for i in range(8)]
    for i in compare:
        if i > 0:
            return False
        if i < 0:
            return True
    return False
    

def multiply(first, second, bit_pattern = False):
    """
    Had to give up on the russian peasant because you sort of need
    something that doesn't overflow when you look at it.
    
    Uses left-shifts and adds.
    
    For each 1 in first, take a copy of second multiplied by the power of 2 
    represented by the 1, and add it.
    
    eg:
               1 0 0 1
               1 0 0 0
         _____________
               1 0 0 0
         1 0 0 0 0 0 0
    
       = 1 0 0 1 0 0 0
       
    
    """
    new_bits = [0]*8
    
    if not bit_pattern:
        first = first.bits
        second = second.bits
    
    for i in zip(second, range(8,0, -1)):
        if i[0] == 1:
            addend = shift_left_n(first, i[1]-1)
            new_bits = add(new_bits, addend, bit_pattern = True)
        
    int_bits = [int(digit) for digit in new_bits]
    
    if bit_pattern:
        return int_bits
    else:
        str_bits = [str(digit) if digit else "0" for digit in new_bits]
        new_int = int("".join(str_bits), 2)
        return new_int


def subtract(first, second, bit_pattern = False):
    
    if not bit_pattern:
        first = first.bits
        second_2C = second.twos_comp_bits

    else:
        #Make the second bits into their 2s comp.
        second_2C = get_2c_bits(second)
        
    #Add, with the magic of 2s comp.
    new_bits = add(first, second_2C, bit_pattern = True)
    int_bits = [int(digit) for digit in new_bits]
    
    if bit_pattern:
        return int_bits
    
    else:
        str_bits = [str(digit) if digit else "0" for digit in new_bits]
        new_int = int("".join(str_bits), 2)
        return new_int


def divide(dividend, divisor, bit_pattern = False, mod = False):
    """
    All glory to https://www2.hawaii.edu/~esb/1998fall.ics312/sep23.html 
    who helped me make sense of this hot mess.
    """
    
    if not bit_pattern:
        dividend = dividend.bits
        divisor = divisor.bits
    
    BITS_2 = [0,0,0,0,0,0,1,0]
    BITS_1 = [0,0,0,0,0,0,0,1]
    
    if sum(divisor) == 0:
        raise ValueError("Division By Zero!")
    
    Q = [0]*8
    R = [0]*8
    div_p = divisor
    
    while div_p[0] != 1:
        div_p = shift_left(div_p)
    while True:
        if less_than(dividend, divisor):
            R = dividend
            break
        Q = multiply(Q, BITS_2, bit_pattern = True)
        if leq(div_p, dividend):
            Q = add(Q, BITS_1, bit_pattern = True)
            dividend = subtract(dividend, div_p, bit_pattern = True)
        div_p = shift_right(div_p)

    int_bits = Q
    
    if mod:
        int_bits = R
    
    if bit_pattern:
        return int_bits
    
    else:
        str_bits = [str(digit) if digit else "0" for digit in int_bits]
        new_int = int("".join(str_bits), 2)
        return new_int
