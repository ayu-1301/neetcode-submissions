class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            my_dict[num] = my_dict.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in my_dict.items():
            buckets[freq].append(num)

        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result