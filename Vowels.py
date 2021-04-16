def vowel(string):
    vowels = ['a','e','i','o','u']
    vowel_count = 0
    for char in list(string.lower()):
        if char in vowels:
            vowel_count += 1
    return vowel_count

if __name__ == '__main__':
    text = 'Hi ThERE?'
    print(vowel(text))