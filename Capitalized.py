def capitalized(string):
    cap_string = ''
    words = []
    #split the string with space
    str_list = string.split(" ")
    for word in str_list:
        #capitalize first word and join the rest of the text
        # words.append(word[0].upper() + word[1:])
        words.append(word.capitalize())
    #join all words together with space
    cap_string = ' '.join(words)

    # you can use list comprehension
    # cap_string = ' '.join([word.capitalize() for word in str_list])
    return cap_string 

#VERSION 1
#check the space of the left side of the words
def capitalized_v1(string):
    cap_string = string[0].upper()
    for i in range(1,len(string)):
        if string[i-1] == ' ':
            cap_string += string[i].upper()
        else:
            cap_string += string[i]
    # cap_string = ' '.join(words)
    print(cap_string)
    return cap_string

if __name__ == '__main__':
    text = 'look, it is working! hi. nihao ma'
    print('Original Text: ',text)
    print('Python built-in: ',text.title())
    print('Capitalized Text: ',capitalized(text))
    print(capitalized_v1(text))