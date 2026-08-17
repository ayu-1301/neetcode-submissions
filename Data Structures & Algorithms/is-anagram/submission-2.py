class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_dict = {}
        for char in s:
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1
        for char in t:
            if  char in my_dict:
                my_dict[char] -= 1
            else:
                return False

        for value in my_dict.values():
            if value != 0:
                return False
        
        return True
