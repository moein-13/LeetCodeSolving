class Solution:
    def scoreOfString(self, s: str) -> int:
        '''score = 0
        for i in range(len(s) - 1 ):
            score += abs( ord (s[i]) - ord (s[i+1]) )
        return score '''

        return sum([ abs( ord(a) - ord(b)) for a, b in pairwise(s) ])