class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for i in num_set:
            if i - 1 in num_set:
                continue
            
            length = 1
            while i + 1 in num_set:
                i += 1
                length += 1

            longest = max(longest, length)
        return longest