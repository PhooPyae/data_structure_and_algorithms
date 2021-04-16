def string_reverse_1(string):
    #version 1
    #less manual work
    return string[::-1]

def string_reverse_2(string):
    #version 2
    #more manual work
    rev = ''
    for char in string:
        rev = char + rev
    return rev

# def string_reverse_3(string):
#     for char in string => return rev = char + rev

# def list_reverse():
#     #version 4
#     #list reverse
#     lst = [0,1,2,3,4]
#     lst.reverse()
#     print('List Reverse',list_reverse(lst))

if __name__ == '__main__':
    string = 'what the hell are you doing?'
    print('String Reverse',string_reverse_1(string))
    print('String Reverse Version 2:',string_reverse_2(string))
    # print(string_reverse_3(string))
