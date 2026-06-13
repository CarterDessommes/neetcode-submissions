class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # amount of coins to make amount a
        memo = [amount + 1] * (amount + 1)

        memo[0] = 0
        
        for a in range(1, amount + 1):
            
            for coin in coins:
                if a - coin >= 0:
                    memo[a] = min(memo[a], 1 + memo[a - coin])
            
        if memo[amount] == amount + 1:
            return -1
    
        return memo[amount]

