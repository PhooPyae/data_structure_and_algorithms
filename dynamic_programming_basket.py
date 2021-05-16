def basket(index):
    value_array = []
    print('for ',index)
    # for item in item_list:
    if index in value_cache:
        print(index,' is cache with value ', value_cache[index])
        return value_cache[index]
    elif index > basket_size:
        return value

    while (index < min(item_list)):
        print(index,'is smaller')
        value = 0
        value_cache[index] = value
        index += 1
    print(index)
    print('cache',value_cache)
    if index >= min(item_list):
        print('it is greater')
        for item in item_list:
            if item <= index:
                print('index item,',index,item)
                print('item value',item_list[item])
                value_array.append(basket(index - item) + item_list[item])
                value = max(value_array)
                index += 1
    #             # value = basket(index-item)
    #             # print('fn',value)
    #             value = [basket(index-item)+item_list[item]]
    #             value_cache[index] = max(value)
    #         index += 1
    #     print(value_cache)
    return value

if __name__ == '__main__':
    value_cache = {}
    value = 0
    index = 0
    basket_size = 5
    item_array = [[]*basket_size for i in range(basket_size)]
    print(item_array)
    item_list = {
        2 : 3,
        3 : 6,
        5 : 10
    }
    # print(min(item_list))
    # print(basket(index))
    basket(index)