class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # first word is a perfect match
        first = strs[0]
        totalLen = len(first)

        for word in strs:

            # loop through for the smaller word
            currLen = 0
            n = min(totalLen, len(word))

            # we increase the range is letters match and break if they don't
            for i in range(n):
                if first[i] == word[i]:
                    currLen += 1
                else:
                    break
            
            # take the min if the range shrinks
            totalLen = min(totalLen, currLen)

        # return the range
        return first[0:totalLen]

                