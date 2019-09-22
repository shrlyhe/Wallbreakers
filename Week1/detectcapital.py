class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        if word.isupper():
            return True
        if word.islower():
            return True
        elif word.istitle():
            return True
        else:
            return False