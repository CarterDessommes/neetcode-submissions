class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        money = {5 : 0, 10 : 0}

        for bill in bills:
            if bill == 5:
                money[5] += 1
            if bill == 10:
                if not money[5]:
                    return False
                money[5] -= 1
                money[10] += 1
            if bill == 20:
                if money[10] and money[5]:
                    money[10] -= 1
                    money[5] -= 1
                elif money[5] >= 3:
                    money[5] -= 3
                else:
                    return False
        
        return True
