class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        adict = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in adict:
                return [adict[diff],i]
            adict[n] = i
        return []
            