class Solution:
    def rob(self, nums: List[int]) -> int:
        R_max = [0 for i in range(len(nums) + 1)]
        R_max[1] = nums[0]
        for i in range(2, len(nums) + 1):
            R_max[i] = max(R_max[i - 2] + nums[i - 1], R_max[i - 1])
        return R_max[len(nums)]
        