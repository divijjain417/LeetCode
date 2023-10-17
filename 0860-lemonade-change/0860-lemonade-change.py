class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill5 = 0
        bill10 = 0
        totalSale = 0
        for i in range (len(bills)):
            change = bills[i] - 5
            if (change == 0):
                bill5 += 1
                totalSale += 5
            elif (change <= totalSale):
                if change == 5 and bill5 >= 1:
                    bill10 += 1
                    bill5 -= 1
                    totalSale += 5
                elif change == 15 and bill5 >= 1:
                    if (bill10 >= 1):
                        bill10 -= 1
                        bill5 -= 1
                        totalSale += 5
                    elif (bill5 >= 3):
                        bill5 -= 3
                        totalSale += 5
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        return 1



        