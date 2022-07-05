list_prices = [1, 25, 24, 23, 12, 36, 14, 40, 31, 41, 5]
temp_profit = []
k = 3
ko = 0
summed_p_list = []


def max_transactions(transactions):
    if transactions > len(list_prices) // 2:
        return len(list_prices) // 2
    else:
        return transactions


def simplifier(prices):
    temp_order = []
    for i, x in enumerate(prices):
        if i != len(prices) - 1 and prices[i - 1] < x <= prices[i + 1]:
            temp_order.append(x)
        elif i != len(prices) - 1 and i != prices[i - 1] > x >= prices[i + 1] and i != 0:
            temp_order.append(x)
    for x in temp_order:
        prices.remove(x)
    return prices


def max_profit(remaining_prices, current_profit, current_k, summed_profit_list):
    current_k += 1
    for idx, prices in enumerate(remaining_prices):
        for ahead_idx, ahead_prices in enumerate(remaining_prices):
            if ahead_idx > idx:
                if current_k == 1:
                    current_profit = [ahead_prices - prices]
                if current_k != 1:
                    current_profit.append(ahead_prices - prices)
                if current_k == k:
                    temp_summed_profit = sum(current_profit)
                    summed_profit_list.append(temp_summed_profit)
                if len(current_profit) == k:
                    current_profit.pop()
                temp_list = remaining_prices.copy()
                for i in range(ahead_idx + 1):
                    if len(temp_list) > 0:
                        temp_list.pop(0)
                if current_k != k:
                    max_profit(temp_list, current_profit, current_k, summed_profit_list)
    current_k -= 1
    return summed_profit_list


new_prices = simplifier(list_prices)
k = max_transactions(k)
max_profit = max(max_profit(new_prices, temp_profit, ko, summed_p_list))
print(f"The max amount of profit possible is {max_profit}")
