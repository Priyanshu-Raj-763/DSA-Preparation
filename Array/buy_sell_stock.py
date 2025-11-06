#we have to find maximum profit from these prices that when we should buy and sell the stock so we will get the max profit

def getMaxProfit(prices):
    max_profit = 0
    min = float('inf')
    for i in range(len(prices)):
        if(prices[i] < min):
            min = prices[i]
        elif(prices[i] - min > max_profit):
            max_profit = prices[i] - min
    return max_profit


prices = [7,4,5,3,6,16]
max_profit = getMaxProfit(prices)
print("The max profit = ",max_profit)
