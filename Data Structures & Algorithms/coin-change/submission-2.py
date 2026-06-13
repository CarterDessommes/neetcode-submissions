class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # amount of coins to make amount a
        # need + 1 in the array initially as we want to take the min 
        # and need amount + 1 on the outside as in the end we want amount
        memo = [amount + 1] * (amount + 1)
        
        # takes 0 coins to make 0 amount
        memo[0] = 0
        
        # for each amount from one on
        for a in range(1, amount + 1):
            # we will try each coin and see if 
            # it is faster to get here using this coin and build
            # of a previous amount
            # need this min as there are cases where we will
            # get here after someting better has got there
            # i.e. 
            for coin in coins:
                if a - coin >= 0:
                    memo[a] = min(memo[a], 1 + memo[a - coin])
            
        if memo[amount] == amount + 1:
            return -1
    
        return memo[amount]

