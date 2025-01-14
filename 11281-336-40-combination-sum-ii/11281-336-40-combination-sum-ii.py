class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        self.dfs(candidates, target, 0, [], result)
        return result
    
    def dfs(self, candidates, target, index, path, result):
        seen = []
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(index, len(candidates)):
            if (candidates[i] in seen):
                continue
            self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], result)
            seen.append(candidates[i])
        