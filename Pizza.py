class Solution():
    def __init__(self):
        pass

    def Pizza(self,n):
        temp = 0
        if n > 7 : 
            temp = n/7

        return temp

Test = Solution()
result = Test.Pizza(97)
print(result)