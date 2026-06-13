class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = [amount + 1] * (amount + 1)

        memo[0] = 0            

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    memo[a] = min(memo[a], memo[a - coin] + 1)
        
        if memo[amount] == amount + 1:
            return -1

        return memo[amount]

