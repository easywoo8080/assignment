def solution(answers):
    answer = [0, 0, 0]
    # print(answers)
    supoja = [
        [1, 2, 3, 4, 5]
        , [2, 1, 2, 3, 2, 4, 2, 5]
        , [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    for i in answers:
        for j in supoja:
            # print('jj',j[0], i)
            # print(j[i%len(j)])
            j_val = j[i%len(j)]
            if( i ==  j_val):
                # answer[j] += 1
                print(i)
    return answer