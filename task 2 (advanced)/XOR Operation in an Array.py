class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        answer = 0
        for i in range(start,start+(n*2),2):
            answer ^= i
        return answer
