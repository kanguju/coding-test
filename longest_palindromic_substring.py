# 가장 긴 팰린드롬 부분 문자열을 출력하라.
##################
# 입력
# "babad"
# 출력
# "bab"
# 설명
# "bab" 외에 "aba"도 정답이다.
##################
# 예제 2
# 입력
# "cbbd"
# 출력
# "bb"

s = "babad"

class Solution():
    def __init__(self):
        pass

    def my_solution(self,s):
        # 1. 팰린드롬을 찾아낸다.
        # 1-1. 나올 수 있는 모든 경우의 수 나열
        # 1-2. 그중에서 팰린드롬인 것을 찾음

        # 2. 가장긴 팰린드롬을 선택한다.

        return
    
    def book(self, s:str):
        # 팰린드롬 판별 및 투 포인터 확장.
        def expand(left: int, right: int) -> str:
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left + 1 : right]
        
        # 해당 사항이 없을때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i+1),
                         expand(i, i+2),
                         key=len)
        return result
    
solution = Solution()
result = solution.book(s)
print(f"[result] {result}")
