# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하시오.  
# - 대소문자 구분은 하지 않는다.  
# - 구두점(마침표, 쉼표 등)은 무시한다.  
# - 입력은 문자열 `paragraph`와 리스트 `banned`가 주어진다.  
# - 금지된 단어(`banned`)에 포함되지 않은 단어 중 가장 많이 나온 단어를 반환하라.

# ✅ 입력   
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# ✅출력
# "ball"

import re,collections

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

class Solution():
    def __init__(self):
        pass

    # my type
    def most_common_word_mytype(self,paragraph,banned):

        # 1. 불순물 제거 [^a-z0-9] 
        
        # 2. 단어 나누기
        letters=paragraph.split()

        # 3. 밴단어 삭제
        list(paragraph)
        for i in range(len(letters)):
            print(f"[letters[i]] {letters[i]} | [banned[0]] {banned[0]}")
            if letters[i] == banned[0]:
                letters[i] = letters[i].replace(letters[i],"")
                print(f"[ letters[i].replace] {letters}")
        print(f"[letters] {letters}")

        # 4. 가장 많이나온 단어 출력.
    
        return
    
    # book type1
    def most_common_word_book_type1(self,paragraph: str,banned: list[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                .lower().split()
                    if word not in banned]
        
        counts = collections.Counter(words)
        #가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]


solution = Solution()
# solution.most_common_word_mytype(paragraph,banned)
result = solution.most_common_word_book_type1(paragraph,banned)
print(f"[result] {result}")