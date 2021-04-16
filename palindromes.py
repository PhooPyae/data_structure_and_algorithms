def palindromes_1(string):
    #version 1
    rev = string[::-1]
    if string == rev:
        return 'Yes'
    return 'No'

def palindromes_2(string):
    #version 2
    rev = ''
    for char in string:
        rev = char + rev
    if string == rev:
        return 'Yes'
    return 'No' 

def palindromes_3(string):
    #version 3
    length = len(string)
    for i in range(int(length/2)):
        if string[i] == string[length-1]:
            length -= 1
        else: return 'No'
    return 'Yes'

if __name__ == '__main__':
    string = 'abbcbba'
    print('Is it Palidromes?',palindromes_1(string))
    print('Is it Palidromes?',palindromes_3(string))