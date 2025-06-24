def maxProfit(prices: List[int]) -> int:
    lowest = 10 **4 + 1
    profit = 0

    for price in prices:
        if price < lowest:
            lowest = price
        if profit < (price - lowest):
            profit = price - lowest
    
    return profit
