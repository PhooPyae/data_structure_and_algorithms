# TO BE CORRECT
# WRONG ANS
# USE STACK
# PUSH OPEN BRACKETS TO STACK AND POP WHEN IT FOUND THE SAME TYPE CLOSED BRACKET


def check_balance(paran_count):
    status = False
    if paran_count['('] == paran_count[')']:
        status = True
    else: status = False
    
    if paran_count['['] == paran_count[']']:
        status = True
    else: status = False

    if paran_count['{'] == paran_count['}']:
        status = True
    else: status = False

    return status

def paran_counter(char, s):
    paran_count = {}
    
    if char in paran_count:
        paran_count[char] += 1
    else:
        if paran_checker(char):
            paran_count[char] = 1

    return paran_count

def paran_checker(char):
    if char == '(':
        return True
    elif char == '{':
        return True
    elif char == '[':
        return True


def isValid(s):
    for char in s:
        paran_count = paran_counter(char, s)
    
    is_valid = check_balance(paran_count)
    
    return is_valid

s = "()"
print(isValid(s))
