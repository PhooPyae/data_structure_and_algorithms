def array_chunk(array,size):
    temp_array = []
    chunked = []
    for n in range(len(array)+1):
        if n == len(array):
            chunked.append(temp_array)
        elif len(temp_array)<size:
            temp_array.append(array[n])
        else: 
            chunked.append(temp_array)
            temp_array = []
            temp_array.append(array[n])
    return chunked
    
if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9]
    size = 3
    print(array_chunk(array,size))