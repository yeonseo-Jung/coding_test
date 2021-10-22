def solution(lottos, win_nums):
    count_zero = 0
    for n in lottos:
        if n == 0:
            count_zero += 1
    
    for i in range(count_zero):
        lottos.remove(0)
        
    conc = 0
    for i in lottos:
        for j in win_nums:
            if i == j:
                conc += 1
                continue
            
    max = conc + count_zero
    min = conc
    if min == 0:
        min = 1
    answer = [7 - max, 7 - min]
    
    return answer