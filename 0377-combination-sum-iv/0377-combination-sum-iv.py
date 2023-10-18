class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        combination = [0 for i in range(target + 1)]
        combination[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if (i - num >= 0):
                    combination[i] += combination[i - num]
            print(combination[i])
        return combination[target]



        