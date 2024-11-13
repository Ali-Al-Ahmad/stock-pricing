"this function calculates the maximum profit can be achieved from a given list"

#    i          0   1  2  3   4  5  6  7   8   9  10  11
#prices_list = [12, 9, 6, 7, 10, 8, 3, 18, 14, 19, 1, 2]   length(prices)=12

def _max_profit(prices):
    total_profit = 0
    buy_price = 0
    sell_price = 0
    length_of_prices = len(prices)
    i = 0

    while i < length_of_prices - 1:

        buy_price = prices[i]
        # find the best price to buy
        while i < length_of_prices - 1 and prices[i+1] < prices[i]:
            buy_price = prices[i+1]
            i += 1

        sell_price = prices[i]
        # find the best price to sell
        while  i < length_of_prices - 1 and prices[i+1] > prices[i]:
            sell_price = prices[i+1]
            i += 1

        # after selling sum the profit
        total_profit += sell_price - buy_price
        i += 1

        # print best but/sell prices with the profit
        print(f"buy({buy_price}) : sell({sell_price}) = {sell_price - buy_price}")
    print("maximum profit:", total_profit)

prices_list = [12, 9, 6, 7, 10, 8, 3, 18, 14, 19, 1]
_max_profit(prices_list)
