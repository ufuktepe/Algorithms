# Kadane's Algorithm
def maxProfit(k, prices):
    # if k >= len(prices)//2: return sum(max(0, prices[i] - prices[i-1]) for i in range(1, len(prices)))

    ans = [[0]*len(prices) for _ in range(k+1)]

    for t in range(1, k+1):
        most = 0
        for i in range(1, len(prices)):
            print(f'\nans[{t - 1}][{i}]={ans[t-1][i]}')
            print(f'most + prices[{i}] - prices[{i - 1}]={most + prices[i] - prices[i-1]}')
            most = max(ans[t-1][i], most + prices[i] - prices[i-1])
            print(f'ans[{t}][{i - 1}]={ans[t][i-1]}')
            ans[t][i] = max(ans[t][i-1], most)
    return ans


k = 2
prices = [5, 7, 1, 10, 8, 20]
x = maxProfit(k, prices)
print(x)