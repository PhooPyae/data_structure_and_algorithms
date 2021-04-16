def vowel(string):
    vowels = ['a','e','i','o','u']
    vowel_count = 0
    for char in list(string.lower()):
        if char in vowels:
            vowel_count += 1
    return vowel_count

from collections import Counter
def vowel2(string):
  char_dict = Counter(string.lower())
  return sum([char_dict['a'], char_dict['e'], char_dict['i'],
    char_dict['o'], char_dict['u']])

if __name__ == '__main__':
    text = 'Hi ThERE?'
    print(vowel(text))
    print(vowel2(text))