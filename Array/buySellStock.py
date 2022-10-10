# Brute Force Approach
def buyAndSellStock(A, n):
    maxP = 0
    for buyDay in range(n):
        buyPrice = A[buyDay]
        for sellDay in range(1, n):
            sellPrice = A[sellDay]
            currentProfit = sellPrice - buyPrice
            maxP = max(maxP, currentProfit)
    return maxP


# Optimal Code
def buySell(A, n):
    maxProfit = 0
    l, r = 0, 1
    while r < n:
        if A[l] < A[r]:
            currentProfit = A[r] - A[l]
            maxProfit = max(maxProfit, currentProfit)
        else:
            l = r
        r += 1
    return maxProfit


if __name__ == "__main__":
    arr = [4, 2, 2, 2, 5, 6, 1, 10]
    result = buyAndSellStock(arr, len(arr))
    print(f"Max Profit : {result}")
    res = buySell(arr, len(arr))
    print(f"Optimization Code For Max Profit : {res}")
