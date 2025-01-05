class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        letter = 0
        prefix = 0
        strs.sort(key=len)
        for letterpos in range(len(strs[0])):
            if letterpos != letter:
                break
            for strsiter in range(1,len(strs)):
                if strs[0][letterpos] == strs[strsiter][letterpos]:
                    prefix += 1
                if prefix == len(strs)-1:
                    letter += 1
                    prefix = 0
        returnstring = ""
        for i in range(letter):
            returnstring += strs[0][i]
        if len(strs) == 1:
            return strs[0]
        else:
            return returnstring