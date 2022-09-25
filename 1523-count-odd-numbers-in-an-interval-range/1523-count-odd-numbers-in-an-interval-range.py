from math import ceil

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = high - low + 1
        return int(count/2) if count%2==0 else (int(count//2) + 1 if low%2!= 0 or high%2!= 0 else int(count//2))
