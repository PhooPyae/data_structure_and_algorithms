def int_reverse_1(number):
    #version 1
    #less manual work
    sign = 0    #if positive
    if number < 0:
        sign = -1
        number = abs(number)
    number = str(number)[::-1]
    if sign == -1:
        return int(number) * -1
    else : 
        return int(number)
    # return string[::-1]

def string_reverse_2(string):
    #version 2
    #more manual work
    rev = ''
    for char in string:
        rev = char + rev
    return rev

if __name__ == '__main__':
    number = 500
    print('Reversed Number',int_reverse_1(number))
