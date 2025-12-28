## 출력 [ 0 , 1 ]
nums = [2, 7, 11, 15]
target = 9

class Solution():
    def __init__(self):
        pass

    def my_solution(self, nums, target):
        # 1. 순서대로 비교
        for i in range(len(nums)):
            # i 인덱스 표시
            index_i = 0
            # 인덱스를 저장할 배열 
            index_arr = [] 

            for j in range(len(nums)):
                # j 인덱스 표시
                index_j = 0
                # 같은경우는 pass
                if i == j:
                    pass
                # 2. target과 일치하면 저장
                if i + j == target:
                    index_arr[i][j] = i , j

                index_j = index_j + 1 

            index_i = index_i + 1 

        # 3. 찾은 인덱스 출력
        print(index_arr)

        return []

Test = Solution()
result = Test.my_solution(nums,target)
