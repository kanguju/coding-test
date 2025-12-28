from typing import List

class Solution():
    def __init__(self):
        pass

    def my_solution(self, height):
        # 1. 예외처리: 입력값이 비어있으면 0 반환
        if not height:
            return 0
        
        n = len(height)
        water_trapped = 0

        # 2. 왼쪽과 오른쪽의 벽 높이를 저장할 리스트 준비
        left_max = [0]*n
        right_max = [0]*n

        # 3. 각 위치에서의 왼쪽 최대 높이 계산
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])

        # 4. 각 위치에서의 오른쪽 최대 높이 계산
        right_max[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            right_max[i] = max(right_max[i+1], height[i])

        # 5. 각 칸에 고이는 빗물의 양 계산    
        for i in range(n):
            water_level = min(left_max[i], right_max[i])
            water_trapped += water_level - height[i]

        return water_trapped
    
    def Book_sol_1(self, height: List[int]) -> int:
        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max,right_max = max(height[left], left_max),max(height[right], right_max)

            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
                
        return volume

    def book_sol_2(self, height: List[int]) -> int:
        stack = []
        volume = 0 

        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다.
                top = stack.pop()

                if not len(stack):
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i],height[stack[-1]]) - height[top]

                volume += distance*waters

            stack.append(i)                
        return volume
    
# --- 실행 부분 ---
if __name__ == "__main__":
    input_data = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    
    sol = Solution()
    # result = sol.my_solution(input_data)
    
    # print(f"입력값: {input_data}")
    # print(f"결과(고인 물의 총량): {result}")
    sol = sol.book_sol_2(input_data)
    print(sol)