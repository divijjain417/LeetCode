class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        length = len(palindrome)
        if length == 1:
            return ""

        isOdd = length % 2
        for i, c in enumerate(palindrome):
            if isOdd and i == length // 2:
                continue
            elif i == length - 1:
                return palindrome[:i] + "b"
            elif c != "a":
                return palindrome[:i] + "a" + palindrome[i + 1:]
        