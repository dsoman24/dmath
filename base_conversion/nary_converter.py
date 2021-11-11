# Convert a number from a number system to another. 

def change_num_base(num, from_base, to_base):
    "Change number systems."
    # Convert number to decimal from a given base
    num = str(num)[::-1]
    dec_num = 0
    for i in range(len(num)):
        dec_num += int(num[i]) * from_base**i
    # Convert decimal to a number base "n"
    base_n = ""
    while dec_num != 0:
        remainder = dec_num%to_base
        dec_num = int((dec_num - remainder)/to_base)
        base_n += str(remainder)
    return base_n[::-1]

