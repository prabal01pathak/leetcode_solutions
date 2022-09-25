class Solution:
    def average(self, salary: List[int]) -> float:
        mn, mx = min(salary), max(salary)
        return (sum(salary) - sum([mn, mx]))/(len(salary) -2)