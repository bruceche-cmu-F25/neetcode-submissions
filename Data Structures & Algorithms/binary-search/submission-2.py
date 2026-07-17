class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if not nums:
        #     return -1
        # midpoint = len(nums) // 2
        # if target > nums[midpoint]:
        #     self.search(nums[midpoint:], target)
        # elif target < nums[midpoint]:
        #     self.search(nums[:midpoint],target)
        # else:
        #     return midpoint
        def binary_search(left, right):
            if left > right:
                return -1

            midpoint = (left + right) // 2

            if target > nums[midpoint]:
                return binary_search(midpoint + 1, right)

            elif target < nums[midpoint]:
                return binary_search(left, midpoint - 1)

            else:
                return midpoint

        return binary_search(0, len(nums) - 1)