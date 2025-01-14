class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(nums, [], result)
        return result

    def dfs (self, nums, permutation, result):
        if not nums:
            result.append(permutation)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], permutation + [nums[i]], result)
        

        