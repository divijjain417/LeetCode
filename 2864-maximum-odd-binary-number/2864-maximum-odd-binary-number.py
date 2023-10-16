class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        result = ''
        sorted_string = ''.join(sorted(s, reverse=True))
        last_index = -1
        flag = 0
        for i in range(len(sorted_string) - 1):
            if (sorted_string[i + 1] == '0'):
                flag = 1
                last_index = i
                result += '0'
                break
            result += sorted_string[i]
        print(last_index)
        if flag == 1:
            result = result + sorted_string[last_index + 1:len(sorted_string) - 1] + '1'
            return result
        return s

        