def decryptPassword(s):
    # Write your code here
    decrypt_password = ""
    digit = []
    index = 0
    
    if len(s) == 1:
        return s
    for i in range(len(s)):
        print('s[i]',s[i])
        if s[i] == '0':
            index = i
            break
        elif s[i].isnumeric():
            digit.append(s[i]) 
            index = i
        else:
            break
    if len(digit) == len(s):
        index = 0

    digit_index = len(digit)
    print('digit', digit)

    while index <= len(s)-1:
        print(index)
        if index == len(s)-1:
            if s[index] == '0':
                return decrypt_password + digit[digit_index-1] 
            return decrypt_password + s[index]
        if s[index] == '0':
            print('digit index', digit[digit_index-1])
            decrypt_password = decrypt_password + digit[digit_index-1]
            digit_index -= 1
            index += 1
        elif s[index].isupper() and s[index+1].islower():
            if index+1 != len(s)-1 and s[index+2] == '*':
                decrypt_password = decrypt_password + s[index+1]
                decrypt_password = decrypt_password + s[index]
                index += 3
            else:
                decrypt_password = decrypt_password + s[index]
                index += 1 
        else:
            decrypt_password = decrypt_password + s[index]
            index += 1
        
    return decrypt_password

if __name__ == '__main__':
    s = '11101'
    print(decryptPassword(s))