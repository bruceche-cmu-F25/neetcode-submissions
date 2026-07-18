class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        temp = []
        for num, cnt in count.items():
            temp.append([cnt, num])
        temp.sort()

        result = []
        while len(result) < k:
            result.append(temp.pop()[1])
        return result
        # sorted_nums = sorted(count.keys(), key = lambda x: count[x], reverse = True)
        # return the highest apperences's number as a list