def maxProfit(prices):
    lowest = float("inf")
    profit = 0


    for i in range(len(prices)):
        if prices[i] < lowest:
            lowest = prices[i]
        
        profit = max(profit, (prices[i] - lowest))
    
    return profit