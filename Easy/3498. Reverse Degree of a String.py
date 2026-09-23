class Solution:
    def reverseDegree(self, s: str) -> int:
        output = 0
        string = 'zyxwvutsrqponmlkjihgfedcba'
        for i in range(len(s)):
            temp = s[i]
            pos = string.index(s[i]) + 1
            s_pos = i+1
            output = output + (pos*s_pos)
        return output