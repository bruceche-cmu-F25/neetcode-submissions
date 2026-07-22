class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return 1
        new_set = set()
        
        for n in nums:
            if n not in new_set:
                new_set.add(n)
        
        result = 1
        for n in new_set:
            count = 1
            while n + 1 in new_set:
                count += 1
                result = max(count, result)
                n += 1
        return result

