class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        longest = 0

        for i in ns:
            if i - 1 not in ns:
                length = 1
                current = i

                while current + 1 in ns:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest