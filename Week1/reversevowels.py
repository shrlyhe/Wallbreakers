class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowelsArr = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] not in vowelsArr:
                i += 1
            if s[j] not in vowelsArr:
                j -= 1
            if s[i] in vowelsArr and s[j] in vowelsArr:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                j -= 1
                i += 1
                
        return "".join(s)
        
 