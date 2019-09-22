class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        intDigits = 0
        stringDigits = ''
        answerArr = []
        
        for digit in digits:
            stringDigits += str(digit)

        intDigits = int(stringDigits) + 1
        stringDigits = str(intDigits)
        
        for char in stringDigits:
            answerArr.append(char)
            
        return answerArr
 