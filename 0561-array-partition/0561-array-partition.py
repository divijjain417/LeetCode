class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        tsum = 0
        n = len(nums)
        i = 0
        while (i < n):
            tsum += nums[i]
            i +=2
        return tsum

        