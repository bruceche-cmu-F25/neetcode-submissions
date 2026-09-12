class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # its recording the frequency and put them in a list
        adict = {}
        for n in nums:
            adict[n] = 1 + adict.get(n , 0)
        result = sorted(adict, key=adict.get,reverse=True)
        return result[0:k]