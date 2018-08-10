# new_bits = [0] * 4
# bits = [1,0,1,0]
# other_bits = [1,0,0,0]
# bits.reverse()
# other_bits.reverse()
#
# carry = 0
# for index, self_digit in enumerate(bits):
#     other_digit = other_bits[index]
#     current_eval = carry + self_digit + other_digit
#     if current_eval == 0:
#         new_bits[index] = 0
#     elif current_eval == 1:
#         new_bits[index] = 1
#     elif current_eval == 2:
#         carry = 1
#         new_bits[index] = 0
#     elif current_eval == 3:
#         carry = 1
#         new_bits[index] = 1
#
# new_bits.reverse()
# new_bits.insert(0, carry)
# str_bits = [str(digit) for digit in new_bits]
# print(int("".join(str_bits), 2)
num_1 = [0,1,0,1,1,0,1,0][::-1] # 90
num_2 = [0,0,1,0,1,1,1,1][::-1] # 47

num_3 = [None,None,None,None,None,None,None,None]
carry = 0
for i in range(len(num_1)):
  digit_1 = num_1[i]
  digit_2 = num_2[i]

  current_eval = digit_1 + digit_2 + carry

  if current_eval == 0:
    num_3[i] = 0
  elif current_eval == 1:
    if carry:
      carry = 0
    num_3[i] = 1
  elif current_eval == 2:
    num_3[i] = 0
    carry = 1
  elif current_eval == 3:
    num_3[i] = 1

try:
    num_3[i+1] = carry
except IndexError:
    pass
num_3.reverse()
for digit in num_3:
    if not digit:
        num_3[num_3.index(digit)] = 0

print(carry)
print(num_3)
num_3 = [str(num) for num in num_3]
num_3_str = "".join(num_3)
print(int(num_3_str, 2))