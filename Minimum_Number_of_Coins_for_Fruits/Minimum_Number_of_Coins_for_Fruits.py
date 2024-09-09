class Solution:
    def minimumCoins(self, prices):
        n = len(prices)
        current = [0] * (n + 1)
        current[0] = 0
        current[1] = prices[0]
        for i in range(2, n + 1):
            current[i] = current[i - 1] + prices[i - 1]
            for j in range(i - 1, 0, -1):
                if 2 * j < i:
                    break
                current[i] = min(current[i], current[j - 1] + prices[j - 1])
        return current[n]

#Sequence Alignment: Value of OPT with Linear Space (TIRADO DO EXEMPLO DO SLIDE)
#Sequence-Alignment(m, n, x1x2...xm, y1y2...yn, , ) {
# for i = 0 to m
# CURRENT[i] = i
# for j = 1 to n
# LASTCURRENT ( vector copy)
# CURRENT[0] j
# for i = 1 to m
# CURRENT[i]  min( [xi, yj] + LAST[i-1],
# + LAST[i],
# + CURRENT[i-1] )
#return CURRENT[m]
#}

