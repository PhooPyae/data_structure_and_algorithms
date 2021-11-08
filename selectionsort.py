# Here we use dictionary data structure to store our count of values mapped to respective names in the above photos
singers={"Selena Gomez": 112, "Taylor Swift": 178,"Ed Sheeran": 230,"Justin Bieber": 90,"John Legend": 190,"Beyoncé": 80}

# We then convert dictionary to list of only count values and in singers_list, it will be like this[112,178,230,90,190,80]
singers_list=list(singers.values())

# Starting from here, we define a function for selection sort
def selectionSort(singers_list):
    #This is an empty list which will later be filled with sorted counting values
    singers_rating = []
    # This works to get length of singers' list,which is 6 and then loop until the end of index
    for i in range(len(singers_list)): 
        #We call findLargest function and search for largest value in the sigers' list and I recommend to look first at next third line
        largest = findLargest(singers_list)
        #We got the largest value by calling findLargest function below and we afterwards remove that largest value from singers_list and then add to our empty list declared above
        singers_rating.append(singers_list.pop(largest))
    #We now have sorted list of count from largest to smallest 
    return singers_rating
# You remember largest variable above that calls for this function? Here we define it with the following code
def findLargest(singers_list):
    #We assume the first value of singers' list as the largest value
    largest= singers_list[0]
    #As we consider the first value of singers' list as the largest value, we make it as the largest index of 0
    largest_index = 0
    #We start from index 1 to the end within the length of singers' list
    for i in range(1, len(singers_list)):
        #You remember selection sort is a comparison-based algorithm as in the first definition I said? Here it compares firstly-initialized value of index 0 with the next successive value of index which is 1. And if the successive index is larger than the first index's value, we set it as our largest value next
        if  singers_list[i] > largest:
            #Here we go...
            largest = singers_list[i]
            #So, now the index of the next largest value is our next largest index
            largest_index = i
    #After updating our largest_index, return it to the function. Don't forget to look back at two skipped lines above :xD
    return largest_index
#After applying selection sort algorithm, we add it to the variable name called favorite_singers
favorite_singers=selectionSort(singers_list)
# Then we print favorite_singers and get the following output
print(favorite_singers)

Output:[230, 190, 178, 112, 90, 80]
