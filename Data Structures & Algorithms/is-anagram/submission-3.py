class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = [0] * 26
        word2 = [0] * 26
        
        for letter in s:
            index = ord(letter) -97
            word1[index] += 1
        for letter in t:
            index = ord(letter) -97
            word2[index] += 1
        
        if word1 == word2:
            return True
        return False

        