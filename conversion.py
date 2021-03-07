def hexaDecimal2Number(hexaVal):  # give decimal value of hex character

    hex = ord(hexaVal)

    if hex >= ord('0'):
        if hex <= ord('9'):  # hexaVal is between '0' and '9'
            return hex - ord('0')  # distance from '0' which is same as decimal value

        elif ord(hexaVal) >= ord('A') and hex <= ord('F'):  # hexaVal is between 'A' and 'F'

            return 10 + hex - ord('A')  # distance from 'A' + 10, which is same as decimal value
        else:
            print('Invalid hexaVal!')


def hexaDecimal2UnSign(hex_value):  # turn hex number into unsigned int
    res = 0
    num_charac = len(hex_value)  # number of characters

    count = 0
    while num_charac > count:  # go through each letter
        res += hexaDecimal2Number(hex_value[count]) * 16**(num_charac-1-count) # adding decimal value of letter multiplied by power of 16 (hex is base 16)
        count += 1

    return res

def hexaDecimal2_SignInt(hex_value):  # turn hex number into signed int
    # num_charact = len(hex_value) # number of characters

    number_of_bytes = len(hex_value) / 2  # 1 byte per 2 characters

    unsigned = hexaDecimal2UnSign(hex_value)  # get the decimal representation of hex number
    power = 2 ** (number_of_bytes * 8 - 1)  # leftest bit equal to 1

    if unsigned < power:  # leftest bit is 0, therefore number is positive
        return int(unsigned)
    else:  # leftest bit is 1 so number is negative
        unsigned -= power  # remove leftest bit
        unsigned -= power  # convert to negative number

        return int(unsigned)

def hexaDecimal2Float(hex_value):  # turn hex number to float
    # number_of_characters = len(hex_value)  # number of characters

    number_of_bytes = int(len(hex_value) / 2)  # 1 byte per 2 characters
    tot_bit = number_of_bytes * 8  # 8 bits per 1 byte

    hex_to_dec = hexaDecimal2UnSign(hex_value)  # decimal version of hex number

    binary = []  # list of bits

    cnt = 0
    while tot_bit > cnt:
        binary.append((hex_to_dec >> (tot_bit - 1 - cnt)) & 1)  # add each bit
        cnt += 1

    whole_bits = 0  # number of exponent bits
    fraction_bits = 0  # number of bits after the dot

    switcher = {1: (4, 3), 2: (6, 9), 3: (8, 15), 4: (10, 21)}

    if number_of_bytes in switcher.keys():
        whole_bits = switcher[number_of_bytes][0]
        fraction_bits = switcher[number_of_bytes][1]
    else:
        print('Too many bytes!')

    if binary[0] == 0:
        sign = 1
    else:
        sign = -1
    whole = 0  # exponent bits represented as a decimal number

    # print(binary) for debugging

    for i in range(0, whole_bits):
        power = pow(2, i)
        # if binary[whole_bits - i] == 1: #  for debugging
        #	print('Adding ' + str(power) + ' to ' + str(whole) + ' and getting ' + str(power + whole)) #  for debugging
        whole += binary[whole_bits - i] * (2**i)

    fraction = 0  # bits after dot represented as a decimal number
    for i in range(0, fraction_bits):
        fraction += binary[tot_bit - 1 - i] * (2**i)

    # print('Whole is ' + str(whole))       #  for debugging
    # print('Fraction is ' + str(fraction)) #  for debugging

    bias = pow(2,(whole_bits - 1)) - 1  # bias
    exponent = whole - bias
    mantissa = 1 - binary[0]  # 1 for positive, 0 for negative

    for i in range(0, fraction_bits):
        mantissa += binary[whole_bits + 1 + i] / pow(2,(i+1)) # add fractional parts to mantissa

    # print('Exponent is ' + str(exponent)) # for debugging
    # print('Mantissa is ' + str(mantissa)) # for debugging

    if binary[0] == 1:  # is a negative number
        exponent += 1  # raise exponent by one

    #    if '0' not in exp_part and ('0' in mantissa and '1' in mantissa):
   
    res = sign * pow(2,exponent )* mantissa  # calculate final result

    a=str(exponent)
    b=str(mantissa)

    # list1= [exponent,mantissa]

    # print(type(exponent),type(mantissa))
    print(exponent,mantissa)
    print(a,b)
    
    if '0' not in a and ('0' in b and '1' in b):
        return 'Nan'
    else:

        return res


if __name__ == '__main__':
    
    hex_number = input('Insert hex here: ')
    convert_type = input('Choose conversion type (S/U/F) : ')

    if len(hex_number) > 8:
        print('Hex number is too big!')
        # return

    if len(hex_number) % 2 == 1:
        hex_number = '0' + hex_number  # if there are odd characters, append '0' to the start

    if convert_type == 'U':
        print(hexaDecimal2UnSign(hex_number))
    elif convert_type == 'S':
        print(hexaDecimal2_SignInt(hex_number))
    elif convert_type == 'F':
        print(hexaDecimal2Float(hex_number))
    else:
        print('Invalid conversion type!')


