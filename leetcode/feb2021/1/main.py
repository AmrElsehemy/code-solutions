class Solution(object):
    def hammingWeight(self, n: int) -> int:
        ones = 0
        for c in ("{0:b}".format(n).zfill(32)):
            if (c == '1'):
                ones = ones + 1
        
        return ones

s = Solution()
answer = s.hammingWeight(9)
print(answer)