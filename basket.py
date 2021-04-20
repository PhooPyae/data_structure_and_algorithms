def basket(basket_size):
    value_cache = {}
    value = 0
    index = 0
    item_list = {
        2 : 3,
        3 : 6,
        5 : 10
    }
    while index <= basket_size:
        # print('Index',index)
        # print('value cache',value_cache)
        if index in value_cache:
            return value_cache[index]
        
        if index < min(item_list):
            # print('it is less than 0')
            value = 0
            value_cache[index] = value
        elif index >= min(item_list):
            value_array = []
            # print('index >= 2')
            for item in item_list:
                if index >= item:
                    # print('difference',value_cache[index-item])
                    value_array.append(value_cache[index - item] + item_list[item])
                    value = max(value_array)
                    value_cache[index]  = value
        index += 1
    return value

if __name__ == '__main__':
    basket_size = 10
    print(basket(basket_size))