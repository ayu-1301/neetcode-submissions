class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        freq = {}
        result = []
        fin = []

        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

        result = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        for key, value in result:
            if len(fin) == k:
                break
            else:
                fin.append(key)

        return fin

        
