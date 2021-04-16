import re

def anagram(string_1,string_2):
    charMap_1 = buildCharMap(string_1)
    charMap_2 = buildCharMap(string_2)
    #check the length of two strings
    if len(charMap_1) != len(charMap_2):
        return False

    #check two character maps
    # for char in charMap_1:
    #     if charMap_1[char] != charMap_2[char]:
    #         return False
    # return True
    return charMap_1 == charMap_2
from collections import Counter
def buildCharMap(string):
    str_dict = {}
    
    #find non alphanumeric and replace with empty string
    string = re.sub(r'\W+', '', string.lower())
    # for char in string:
    #     if (re.match('^\W+$',char)):
    #         string =string.replace(char,'').lower()
    
    #build a character map / a dictionary {'h':1.'e',1}
    # for char in string:
    #     if (not char in str_dict):
    #         str_dict[char] = 1
    #     else:
    #         str_dict[char] = str_dict[char] + 1
    str_dict = Counter(string)
    return str_dict

#------------------------------
#ANOTHER VERSION 1
#more straightfoward and alternative one
#compare two sorted string
def anagram_v1(string_1,string_2):
    print(cleanString(string_1))
    print(cleanString(string_2))
    return cleanString(string_1) == cleanString(string_2)

#remove non alphanumeric characters
#sort the string
def cleanString(string):
    # sorted_string = ''
    string = re.sub(r'\W+', '', string.lower())
    # for char in string:
    #     if (re.match('^\W+$',char)):
    #         string =string.replace(char,'').lower()

    return ''.join(sorted(list(string)))
#-------------------------------

if __name__ == "__main__":
    text_1 = 'RAIL Safety!'
    text_2 = 'FAIRY TALES'
    print('Is that Anagrams?',anagram(text_1,text_2))
    print('Is that Anagrams?',anagram_v1(text_1,text_2))
