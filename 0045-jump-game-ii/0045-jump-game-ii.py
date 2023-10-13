# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums) - 1
#         m = len(nums)
#         i = 0
#         j = 1
#         k = 0
#         r = nums[0]
#         max_stop = -1
#         stops = [0]
#         if (m == 1):
#             return 0
#         while (i < m) :
#             maximum = -1
#             if (nums[i] >= n):
#                 break
#             for k in range(j, j + r) :
#                 if (((k - i) + nums[k]) >= maximum):
#                     maximum = (k - i) + nums[k]
#                     max_stop = k
#             n -= (max_stop-i)        
#             stops.append(max_stop)
#             i = max_stop
#             j = k
#             r = nums[max_stop] - (j - max_stop - 1)
        
#         print(stops)
#         return len(stops)
    
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums) - 1
        m = len(nums)
        i = 0
        currDistance = nums[0]
        max_stop = 0
        maximum = -1
        stops = [0]
        if (m == 1):
            return 0
        for j in range(1, m) :
            if (nums[i] >= n):
                break
            elif (currDistance == j):
                if (((j - i) + nums[j]) >= maximum):
                    maximum = (j - i) + nums[j]
                    max_stop = j
                currDistance = nums[max_stop] - (j - max_stop) + j;
                stops.append(max_stop)
                maximum = -1
                n -= (max_stop-i)
                i = max_stop
            else:
                if (((j - i) + nums[j]) >= maximum):
                    maximum = (j - i) + nums[j]
                    max_stop = j
        print(stops)
        return len(stops)