class Solution:
    def isAnagram(self, s: str, t: str) -> bool:    
        if len(s) != len(t):
            return False

        my_dict = {}

        for i in s:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        
        for i in t:
            if i in my_dict:
                my_dict[i] -= 1
            else:
                return False
        
        for count in my_dict.values():
            if count != 0:
                return False
        
        return True
