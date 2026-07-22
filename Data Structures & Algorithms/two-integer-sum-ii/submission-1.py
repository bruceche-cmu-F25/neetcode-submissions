class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        
        # if numbers[0] > target:
        #     return []
        
        # if numbers[0] + numbers[-1] < target:
        #     return []
        
        left = 0
        right = len(numbers) - 1

        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return [left + 1, right + 1]
