class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reversedString = ''
        s = s.split()
        for word in s:
            reversedString += self.reverseIndivWord(word) + ' '
        
        return reversedString.strip()
                
    
    def reverseIndivWord(self, s):
        i = 0
        j = len(s) - 1
        s = list(s)
        newString = ""
        
        while i < j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1
        
        return newString.join(s)
            