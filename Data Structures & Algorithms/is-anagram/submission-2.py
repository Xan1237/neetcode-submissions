class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}

        for letter in s:
            letters[letter] = letters.get(letter, 0) + 1
            
        print(letters)
        for letter in t:
            if letters.get(letter, 0) != 0:
                letters[letter] -= 1
            else:
                return False
        
        print(letters.values())
        for letter in letters.values():
            if letter != 0:
                return False
        return True