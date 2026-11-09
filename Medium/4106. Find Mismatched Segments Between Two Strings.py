class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:

        result = []
        n = len(s1)
        m = len(s2)

        i=0
        while i<n:

            if s1[i] == s2[i]:
                i = i+1
            else:
                sub1 = ''
                sub2 = ''

                while i<n and s1[i]!=s2[i]:
                    sub1 += s1[i]
                    sub2 += s2[i]
                    i = i+1

                result.append([sub1,sub2])

        return result
            