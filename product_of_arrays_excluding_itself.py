data = [1,2,3,4]

class Solution():
    def __init__(self):
        pass

    def my_sol_1(self,data:list[int]) -> int:
        
        for i,r in enumerate(data):
            
            # 원본 데이터 유지 
            # while문 사용

            # 1. 자신을 제외한다.
            data.pop(i)

            result = []

            # 2. 나머지를 곱한다.
            for i in range(data):

                pass    
            
        pass

    def my_sol_2(self,data:list[int]) -> int:

        exe = 0 # 제외할 데이터
        result = [] # 결과 저장할 공간
        product = 1 # 곱을 저장할 공간

        for i,r in enumerate(data):
            
            # 1. 자신을 제외한다.
            exe = data.pop(i)

            # 2. 나머지를 곱한다.
            for i_2 in range(len(data)):
                product = product*data[i_2]

            # 3. 결과 저장
            result.insert(i,product)
            
            # 4. 초기화
            data.insert(i,exe)
            product = 1

        return result
    
    def book_sol_1(self,nums:list[int]) -> list[int]:
        out = []
        p = 1
        # 왼쪽 곱샘
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        # 왼쪽 곱샘 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums) -1 , -1 , -1):
            out[i] = out[i]*p
            p = p * nums[i]
        
        return out

sol = Solution()
print(f"원본 데이터 : {data}")
print(f"자기 자신을 제외한 배열들의 곲 : {sol.my_sol_2(data)}")
print(f"자기 자신을 제외한 배열들의 곲 : {sol.book_sol_1(data)}")