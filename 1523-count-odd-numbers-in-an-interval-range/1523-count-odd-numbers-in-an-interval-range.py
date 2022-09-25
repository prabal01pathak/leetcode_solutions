from math import ceil

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = int(high - low)//2
        return (
            count + 1
            if low%2!= 0 or high%2!= 0
            else count
        )
