class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # remove dupes
        longest = 0 # placeholder

        for num in numSet:
            if (num-1) not in numSet: # this will keep going till we hit the minimum
                length = 1 # smallest sequence length
                while (num + length) in numSet: # smart increment and check if sequence possible
                    length += 1
                longest = max(length, longest) # we either have a sequence or no sequence
        return longest
        