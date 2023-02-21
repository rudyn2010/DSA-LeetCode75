class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapOne = {}
        mapTwo = {}
        
        for i in range(len(s)):
            char1, char2 = s[i], t[i]
            
            if ((char1 in mapOne and mapOne[char1] != char2) or
               (char2 in mapTwo and mapTwo[char2] != char1)):
                return False
            
            mapOne[char1] = char2
            mapTwo[char2] = char1
            
        return True