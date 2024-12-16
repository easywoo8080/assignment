import time

test_case = []  # 전역 변수로 선언
test_case.append([["apple", "banana", "cherry"], ["banana", "kiwi", "melon", "apple"]])
# test_case.append(27)
# test_case.append(12345)

class Problem:
    '''
    문제 내용
    '''

class Solution(Problem):

    def polynomial_hash(self,s):
        p = 31  # 소수
        m = 1_000_000_007  # 버킷 크기
        hash_value = 0
        # print(s)
        for char in s:
            hash_value = (hash_value * p + ord(char)) % m
            # print(hash_value)
        return hash_value

    def solution(self, string_list, query_list):
        # string_list의 각 문자열에 대해 다항 해시값을 계산
        hash_list = [self.polynomial_hash(s) for s in string_list]
        # print(hash_list)
        # query_list의 각 문자열이 string_list에 있는지 확인
        result = []
        for query in query_list:
            
            query_hash = self.polynomial_hash(query)
            if query_hash in hash_list:
                result.append(True)
            else:
                result.append(False)
        return result


# Object creation and method call (객체 생성 및 메서드 호출)
sol = Solution()
start_time = time.time()
print( [sol.solution(t[0], t[1]) for t in test_case] )
elapsed_time = time.time() - start_time
print(f"Time: {elapsed_time:.6f} seconds")