from typing import List

class Solution():
    def __init__(self):
        pass

    def my_sol(self,nums):
        # 1. 정렬
        nums.sort() 
        results = []
        
        for i in range(len(nums)-2) :
            # 중복된 첫 번째 숫자는 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # 2. 나머지 두 숫자를 찾기
            left, right = i + 1, len(nums) - 1

            while left < right:
                sum_val = nums[i] + nums[left] + nums[right]

                if sum_val == 0 :
                    results.append([nums[i],nums[left],nums[right]])
                    # 중복된 숫자 건너뛰기
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1  
                elif sum_val < 0:
                    left += 1 
                else:
                    right -= 1  
        return results
    
    def book_sol_1(self, nums:List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        # 브루트 포스 n^3 반복
        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums) - 1):
                if j > i +1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j+1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i],nums[j],nums[k]])  

        return results
    
    def book_sol_2(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # 간격을 좁혀가며 합 sum 계산
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0 :
                    right -= 1
                else:
                    # sum = 0인 경우이므로 정답 및 스킵 처리
                    results.append([nums[i],nums[left],nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left +=1
                    while left < right and nums[right] == nums[right - 1]:
                        right -=1                       
                    left += 1
                    right -= 1 
            
        return results


nums = [-1,0,1,2,-1,-4]

sol = Solution()
print(sol.book_sol_2(nums))