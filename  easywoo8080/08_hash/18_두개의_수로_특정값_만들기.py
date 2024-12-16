import time

test_case = []  # 전역 변수로 선언
test_case.append([[1,2,3,8],6])
# test_case.append([[2,3,5,9],10])
# test_case.append(27)
# test_case.append(12345)

class Problem:
    '''
    문제 내용
    '''

class Solution(Problem):

    def count_sort(self, arr, k):
        # 1해시테이블생성및초기화 
        hashtable = [0] * (k + 1)
        print(hashtable)
        for num in arr :
        #현재원소의값이k 이하인때에만처리
            if num <= k:
                # 현재원소의값을 인덱스로해 해당인덱스의해시테이블값을1 로 설정
                hashtable[num] = 1 

        print(hashtable[0])
        print(hashtable)
        return hashtable
            
    def solution(self, arr, target):
        hashtable = self.count_sort(arr, target)
        for num in arr:
            complement = target - num
            # t arget에서현재원소를뺀값이해시테이블에있는지확인 
            if (
                complement != num
                and complement >= 0
                and complement <= target
                and hashtable[complement] == 1
            ):
                return True 
        return False

# Object creation and method call (객체 생성 및 메서드 호출)
sol = Solution()
start_time = time.time()
print( [sol.solution(t[0], t[1]) for t in test_case] )
elapsed_time = time.time() - start_time
print(f"Time: {elapsed_time:.6f} seconds")