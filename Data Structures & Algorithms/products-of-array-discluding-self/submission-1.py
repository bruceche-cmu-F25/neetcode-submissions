class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        result = []
        for i in range(len(nums)):
            pro = 1
            for j in range(len(nums)):
                if not i == j:
                    pro *= nums[j]
                    j += 1
                j += 1
            result.append(pro)
        return result