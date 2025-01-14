class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        path = []
        self.dfs(candidates, 0, path, result, target)
        return result

    def dfs(self, candidates, index, path, result, target):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(index, len(candidates)):
            self.dfs(candidates, i, path + [candidates[i]], result, target - candidates[i])        



        