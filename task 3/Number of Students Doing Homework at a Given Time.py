class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(1 for x, y in zip(startTime, endTime) if queryTime >= x and queryTime <= y)

