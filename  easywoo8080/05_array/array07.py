# 07 방문 길이 **
test_case = ["ULURRDLLU", "LULLLLLLU", "ULLLLLLL"]

def solution(dirs):
    answer = set()
    # print(dirs)

    x,y = 0,0

    #이동 규칙
    move = {
        'U' : (0, 1)
        ,'R' : (1, 0)
        ,'D' : (0, -1)
        ,'L' : (-1, 0)
    }

    #리미트 한도
    limit= {
        'U':5
        ,'R':5
        ,'D':5
        ,'L':5
    }

    for char in dirs:
        # print(char)  # 각 문자를 출력
        # print( x + move[char][0] )
        move_x = x + move[char][0]
        move_y = y + move[char][1]
        if( -limit[char] <= move_x <= limit[char] and -limit[char] <= move_y <= limit[char]):
            # print((x,y), (move_x, move_y))
            load = {(x,y, move_x, move_y)}
            # print(load)
            answer.add(frozenset(load))
            x, y = move_x, move_y

    # print(answer)
    # print('')
    # for path in answer:
        # print(list(path))  # 각 경로를 리스트로 출력
    return len(answer)




print( solution(test_case[1]))
# test_case의 각 요소를 solution 함수에 전달
# print(list(map(solution, test_case)))

# 각 리스트를 정렬하고 결과를 리스트로 반환
# result = [solution(t) for t in test_case]
# print(result)  # 각 리스트가 정렬된 결과 리스트로 출력됩니다.P



def solution(dirs):
    visited = set()
    x, y = 0, 0
    
    moves = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }
    
    for move in dirs:
        nx, ny = x + moves[move][0], y + moves[move][1]

        print('nx : ',x,y , nx , ny)
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            path = {(x, y), (nx, ny)}
            visited.add(frozenset(path))
            x, y = nx, ny

    return len(visited)

# 테스트
print(solution(test_case[1]))  # 출력: 7









