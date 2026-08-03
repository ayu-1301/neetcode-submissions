class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}

        for my_str in strs:
            key = ''.join(sorted(my_str))

            if key in my_dict:
                my_dict[key].append(my_str)
            else:
                my_dict[key] = [my_str]

        return list(my_dict.values())