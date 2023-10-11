class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums) - 1
        m = len(nums)
        i = 0
        j = 1
        k = 0
        r = nums[0]
        max_stop = -1
        stops = [0]
        if (m == 1):
            return 0
        while (i < m) :
            maximum = -1
            if (nums[i] >= n):
                break
            for k in range(j, j + r) :
                if (((k - i) + nums[k]) >= maximum):
                    maximum = (k - i) + nums[k]
                    max_stop = k
            n -= (max_stop-i)        
            stops.append(max_stop)
            i = max_stop
            j = k
            r = nums[max_stop] - (j - max_stop - 1)
        
        print(stops)
        return len(stops)