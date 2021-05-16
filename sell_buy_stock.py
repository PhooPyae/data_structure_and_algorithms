# # def find_next_val(val, prices):
# #     if val in prices:
    
# difference = 0

# def maxProfit(prices):
#     maximum = max(prices)
#     len_price = len(prices)

#     if difference != 0:
#         for i in prices:
#             if +difference >= prices[i]:

#     if len_price < 3 and prices[len_price-1] > prices[len_price-2]:
#         return prices[len_price - 1] - prices[len_price - 2]

#     for i in range(len_price):
#         if prices[i] != maximum:
#             difference = maxProfit(prices[i:]) - maximum
#             # difference = prices[i] - maximum
#         else:
#             break
#     return



# def maxProfit(prices):
#     difference = 0
#     current_max = max(prices)
#     current_min = prices[0]

#     for i in range(len(prices)):
#         if prices[i] <= current_min and prices[i] != current_max:
#             temp_max = max(prices[i:])
#             print('temp max', temp_max)
#             if (temp_max - prices[i]) > difference:
#                 current_min = prices[i]
#                 difference = temp_max - prices[i]
#     return difference

def maxProfit(prices):
    current_min = prices[0]
    difference = 0
    temp_min = prices[0]

    for i in range(len(prices)):
        if temp_min > prices[i]:
            temp_min = prices[i]

        print('price of i', prices[i])
        value = prices[i] - temp_min
        print('value', value)
        if value > difference:
            difference = value
            current_min = temp_min
    return difference

if __name__ == '__main__':
    # difference = 0
    prices = [7,6,4,3,1]
    print(maxProfit(prices))