class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict = {}
        tDict = {}
        
        for char in s:
            if char in sDict:
                sDict[char] = sDict[char]+1
            else:
                sDict[char] = 1
        
        for char in t:
            if char in tDict:
                tDict[char] = tDict[char]+1
            else:
                tDict[char] = 1
        
        for entry in sDict:
            if sDict.get(entry) != tDict.get(entry):
                return False
        
        for entry in tDict:
            if tDict.get(entry) != sDict.get(entry):
                return False
        
        return True