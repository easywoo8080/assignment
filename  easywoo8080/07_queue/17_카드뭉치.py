from collections import deque
import time

test_case = []  # 전역 변수로 선언
test_case.append([["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]])
# test_case.append(27)
# test_case.append(12345)

class Problem:
    '''
    문제 설명
    코니는 영어 단어가 적힌 카드 뭉치 두 개를 선물로 받았습니다. 코니는 다음과 같은 규칙으로 카드에 적힌 단어들을 사용해 원하는 순서의 단어 배열을 만들 수 있는지 알고 싶습니다.

원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용합니다.
한 번 사용한 카드는 다시 사용할 수 없습니다.
카드를 사용하지 않고 다음 카드로 넘어갈 수 없습니다.
기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없습니다.
예를 들어 첫 번째 카드 뭉치에 순서대로 ["i", "drink", "water"], 두 번째 카드 뭉치에 순서대로 ["want", "to"]가 적혀있을 때 ["i", "want", "to", "drink", "water"] 순서의 단어 배열을 만들려고 한다면 첫 번째 카드 뭉치에서 "i"를 사용한 후 두 번째 카드 뭉치에서 "want"와 "to"를 사용하고 첫 번째 카드뭉치에 "drink"와 "water"를 차례대로 사용하면 원하는 순서의 단어 배열을 만들 수 있습니다.

문자열로 이루어진 배열 cards1, cards2와 원하는 단어 배열 goal이 매개변수로 주어질 때, cards1과 cards2에 적힌 단어들로 goal를 만들 있다면 "Yes"를, 만들 수 없다면 "No"를 return하는 solution 함수를 완성해주세요.


제한사항
1 ≤ cards1의 길이, cards2의 길이 ≤ 10
1 ≤ cards1[i]의 길이, cards2[i]의 길이 ≤ 10
cards1과 cards2에는 서로 다른 단어만 존재합니다.
2 ≤ goal의 길이 ≤ cards1의 길이 + cards2의 길이
1 ≤ goal[i]의 길이 ≤ 10
goal의 원소는 cards1과 cards2의 원소들로만 이루어져 있습니다.
cards1, cards2, goal의 문자열들은 모두 알파벳 소문자로만 이루어져 있습니다
    '''

class Solution(Problem):

    def solution(self, cards1, cards2, goal):
        answer = ''
        
        card_1 = deque(cards1)
        card_2 = deque(cards2)
        aim = deque(goal)
        
        while aim:
            if card_1 and card_1[0] == aim[0]:
                card_1.popleft()
                aim.popleft()
            elif card_2 and card_2[0] == aim[0]:
                card_2.popleft()
                aim.popleft()
            else:
                break
        
        if aim :
            answer = 'No'
        else:
            answer = 'Yes'
            
                
        
        
        return answer
    


    def solution_else(cards1, cards2, goal):
        for g in goal:
            if len(cards1) > 0 and g == cards1[0]:
                cards1.pop(0)       
            elif len(cards2) >0 and g == cards2[0]:
                cards2.pop(0)
            else:
                return "No"
        return "Yes"

# Object creation and method call (객체 생성 및 메서드 호출)
sol = Solution()
start_time = time.time()
print( [sol.solution(t[0], t[1], t[2]) for t in test_case] )
elapsed_time = time.time() - start_time
print(f"Time: {elapsed_time:.6f} seconds")