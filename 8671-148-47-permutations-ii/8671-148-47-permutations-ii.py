class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        self.dfs(0, nums, [], result)
        return result

    def dfs (self, index, nums, permutation, result):
        if not nums:
            result.append(permutation)
            return
        for i in range(len(nums)):
            if (i > index and nums[i] == nums [i - 1]):
                continue
            self.dfs(0, nums[:i] + nums[i+1:], permutation + [nums[i]], result)


        