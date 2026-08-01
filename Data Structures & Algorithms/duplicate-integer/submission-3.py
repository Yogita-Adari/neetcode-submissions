class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set(nums)
        if len(nums) == len(seen):
            print(f"nums {nums} seen {seen}")
            return False
        return True