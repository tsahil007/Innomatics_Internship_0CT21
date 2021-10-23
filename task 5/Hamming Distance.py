class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = bin(x)[2:].zfill(32)
        y_bin = bin(y)[2:].zfill(32)
        return sum(1 for x,y in zip(x_bin,y_bin) if x!=y)