class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, n in enumerate(nums):
            nums_dict[n] = i
        
        for i, n in enumerate(nums):
            difference = target - n
            if difference in nums_dict and nums_dict[difference] != i:
                return [i, nums_dict[difference]]
        return []