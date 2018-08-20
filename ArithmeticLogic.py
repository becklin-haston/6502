
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
    
def times_2(bit_pattern):
    #a shimmy-shimmy-shimmy-shimmy-shimmy to the left.
    
    bit_new = [0]*8
    for i in range(8):
        if bit_pattern[i] == 1:
            if i-1 == -1:
                raise ValueError("This number is too large to be doubled.")
            bit_new[i-1] = 1
    return bit_new


def times_2_n(bit_pattern, n):
    for i in range(n-1):
        bit_pattern = times_2(bit_pattern)
    return bit_pattern


def over_2(bit_pattern):
    #a shimmy-shimmy-shimmy-shimmy-shimmy to the right.
    bit_new = [0]*8
    for i in range(8):
        if bit_pattern[i] == 1:
            if i+1 > 7:
                pass #Hope you wanted integer division!
            else:
                bit_new[i+1] = 1
    return bit_new
    

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
            addend = times_2_n(first, i[1])
            new_bits = add(new_bits, addend, bit_pattern = True)
        
    int_bits = [int(digit) for digit in new_bits]
    
    if bit_pattern:
        return int_bits
    else:
        str_bits = [str(digit) if digit else "0" for digit in new_bits]
        new_int = int("".join(str_bits), 2)
        return new_int

