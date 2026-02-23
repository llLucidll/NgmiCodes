### Problem 

You are given a list of n stocks. Each stock is represented as a list of (date, shares) tuples, where date is a string in "M/D" format and shares is a positive integer representing the cumulative number of shares held for that stock on that date.

Between recorded dates for a given stock, its share count remains unchanged (i.e., carries forward from the last recorded value). Before a stock's first recorded date, its share count is considered 0.

Return a list of (date, totalShares) tuples representing the total number of shares held across all stocks on each unique date that appears in the input, sorted in chronological order.


## Example 1
Input: stocks = [
    [("5/1", 100), ("5/5", 200)],           # PLTR
    [("5/5",  50), ("5/8", 100)],            # AAPL
    [("5/1", 200), ("5/8", 100)]             # TSLA
]

Output: [("5/1", 300), ("5/5", 450), ("5/8", 400)]


## Example 2:
Input: stocks = [
    [("1/1", 50)],
    [("1/1", 50), ("1/3", 100)]
]

Output: [("1/1", 100), ("1/3", 150)]