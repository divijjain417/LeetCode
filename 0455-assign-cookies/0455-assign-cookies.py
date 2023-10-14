class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        children = 0
        d = 0
        n = len(s)
        m = len(g)
        for i in range (n):
            if (children == m or d == m):
                break
            if (g[d] <= s[i]):
                children += 1
                d += 1
            else:
                i += 1
        return children

            
        