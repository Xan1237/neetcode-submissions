class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            temp = [0] * 26
            for i in range(len(word)):
                temp[ord(word[i])-97] += 1
            hashmap[tuple(temp)].append(word)
        
        return list(hashmap.values())
        