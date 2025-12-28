data = [1,2,3,4]

class Solution():
    def __init__(self):
        pass

    def my_solution(self,data):
        # 1. 큰수 페어찾기
        for i,v in range(data):
            # 인덱스 저장용
            result = []
          
            max = 0

            # 가장 큰수 찾기
            if v > max :
                max = v
                result = [i,v]
                
            
            # 두번째로 큰 수 찾기
            # ... 

            # data에서 페어 제거하기

            pass

        # 2. 나머지 큰수 페어찾기

        # ...

        pass

    def my_solution_2(self,data):
        total_sum = 0

        # 원본 데이터를 수정하지 않기 위해 복사본 사용
        nums = data.copy()

        # 데이터가 다 없어질 떄 까지 반복
        while len(nums) > 0:
            # 1. 가장 큰 수 찾기
            max_val = max(nums)
            nums.remove(max_val)

            # 2. 두번째로 큰 수 찾기 
            next_max_val = max(nums)
            nums.remove(next_max_val) # 찾은 두 번째 큰수 제거

            # 3. min(가장큰수, 두번째큰수)를 합계에 더하기
            total_sum += min(max_val, next_max_val)

        return total_sum

    def book_solution_1(self, nums: list[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum
    
    def book_solution_2(self,nums: list[int]) -> int:
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            # 짝수 번째 값의 합 계산 , 0부터 시작하므로
            if i % 2 == 0:
                sum += n

        return sum
    
    def book_solution_3(self,nums: list[int]) -> int:
        return sum(sorted(nums)[::2])
    

sol = Solution()
print(f"my_sol_2 결과 : {sol.my_solution_2(data)}")
print(f"book_sol_1 결과 : {sol.book_solution_1(data)}")
print(f"book_sol_2 결과 : {sol.book_solution_2(data)}")
print(f"book_sol_3 결과 : {sol.book_solution_3(data)}")
