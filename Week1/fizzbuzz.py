class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fizzBuzzArr = []
        i = 1
        
        while i <= n:
            if i % 3 is 0 and i % 5 is 0:
                fizzBuzzArr.append("FizzBuzz")
            elif i % 3 is 0:
                fizzBuzzArr.append("Fizz")
            elif i % 5 is 0:
                fizzBuzzArr.append("Buzz")           
            else:
                fizzBuzzArr.append(str(i))
                
            i += 1
        
        return fizzBuzzArr
            
  