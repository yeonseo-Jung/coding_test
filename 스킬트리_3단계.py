def solution(n, computers):
    check = list(range(0, n))
    i = 0
    networks = []
    while True:
        check.remove(i)

        cnt_q = []
        coms = []
        cnt_q.append(i)
        while True:      
            coms.append(i)
            del cnt_q[0]
            j = 0
            for s in computers[i]:
                if i != j and s == 1: 
                    if j in check:
                        cnt_q.append(j)
                        check.remove(j)
                j += 1

            if len(cnt_q) == 0:
                break
            else:
                i = cnt_q[0]

        networks.append(coms)

        if len(check) == 0:
            break
        else:
            i = check[0]

    answer = len(networks)
    return answer