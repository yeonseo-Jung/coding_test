def solution(rows, columns, queries):
    # 주어진 rows, columns값에 따라 1부터 rows*columns까지의 원소를 갖는 이중리스트 생성함
    list_double = []
    list_single = []
    for i in range(1, rows*columns + 1):
        list_single.append(i)
        if i % columns == 0:
            list_double.append(list_single)
            list_single = []      
    
    answer = []
    for s in queries:
        # 주어진 queries에 따라 시계방향 순서로 (rows, columns)값(index)을 리스트에 할당 
        r1 = s[0] - 1
        c1 = s[1] - 1
        r2 = s[2] - 1
        c2 = s[3] - 1
        list_index = []
        r = r1
        c = c1
        while True:  
            list_index.append((r, c))
            if c < c2:
                c += 1
            else:
                break
        while True:
            if r < r2:
                r += 1
                list_index.append((r, c))
            else:
                break
        while True:
            if c > c1:
                c -= 1
                list_index.append((r, c))
            else:
                break
        while True:
            if r > r1 + 1:
                r -= 1
                list_index.append((r, c))
            else:
                break  
        # list_double에서 주어진 queries에 맞게 시계방향 순서로 원소를 추출해서 리스트에 할당 
        list_elem = []
        for t in list_index:
            r = t[0]
            c = t[1]
            list_elem.append(list_double[r][c])
        # 시계방향으로 한칸씩 회전 된 순서대로 리스트에 할당 
        l = [list_elem[-1]]
        list_elem.pop(-1)
        list_elem = l + list_elem

        # 시계방향으로 회전 된 원소들을 list_double에 할당 
        for i in range(len(list_index)):
            rows = list_index[i][0]
            columns = list_index[i][1]
            list_double[rows][columns] = list_elem[i]
        
        # 회전 후 이동한 숫자 중 최솟값 구하기 
        answer.append(min(list_elem))
        
    return answer