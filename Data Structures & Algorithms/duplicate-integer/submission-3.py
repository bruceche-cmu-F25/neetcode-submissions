class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        aset = set()
        for n in nums:
            aset.add(n)
        if len(nums) != len(aset):
            return True
        return False