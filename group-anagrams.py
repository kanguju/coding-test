# 문자열 배열을 받아 애너그램 단위로 그룹화하라.

# ▶ 입력
# ["eat", "tea", "tan", "ate", "nat", "bat"]

# ▶ 출력
# [
#   ["ate", "eat", "tea"],
#   ["nat", "tan"],
#   ["bat"]
# ]

# 📘 참고 | ‘애너그램’이란
# 일정의 언어유희로 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것을 말한다. ‘아구전철(語句轉綴)’이라고도 부르며, 과거 유럽에서는 근대까지 이러한 언어유희가 매우 유행했다고 한다. 애너그램의 우리말 예로는 ‘문전박대’를 ‘대박전문’으로 바꿔 부르는 데에 둥을 둘 수 있다.

import collections

input = ["eat", "tea", "tan", "ate", "nat", "bat"]

class Solution():
    def __init__(self):
        pass

    def group_anagrams_mytype(self,input):
        
        # 1. 각 단어를 쪼개서 딕셔너리로 만듬
        # 2. 키 별로 단어를 비교해서 일치하는 경우에 묶음

        return
    
    def group_anagrams_booktype_1(self, strs: list[str]) -> list[list[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)

        print(f"[anagrams] {anagrams}")

        return list(anagrams.values())
    
solution = Solution()
result = solution.group_anagrams_booktype_1(input)
print(f"[result] {result}")
    