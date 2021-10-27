# 2차 시도
# 효율성 실패
def solution(info, query):
    info_dict = {"cpp": "a1", "java": "a2", "python": "a3",
                "frontend": "b1", "backend": "b2",
                "junior": "c1", "senior": "c2", 
                "chicken": "d1", "pizza": "d2"}

    # info배열을 이중리스트에 할당
    # 사람별, 정보별로 데이터를 분리시키기 위함
    info_double_list = []
    for s in info:
        info_elem = s.split(" ")
        info_double_list.append(info_elem)
    # 점수 정보와 나머지 정보를 한 묶음으로 해서 한 사람의 info데이터를 두개 정보로 분리 
    info_val = []
    for i in info_double_list:
        val = ""
        for j in i[0:4]:
            val += info_dict[j]
        info_val.append([val, int(i[4])])
    # 점수기준 오름차순 정렬    
    info_val = sorted(info_val, key=lambda x:x[1])

    # query배열을 이중리스트에 할당
    # 사람별, 정보별로 데이터를 분리시키기 위함
    query_double_list = []
    for s in query:
        query_elem = s.split(" and ")
        elem = query_elem[-1].split(" ")
        del query_elem[-1]
        query_elem = query_elem + elem
        query_double_list.append(query_elem)  

    # 점수 정보와 나머지 정보를 한 묶음으로 해서 한 사람의 query데이터를 두개 정보로 분리 
    query_val = []
    for i in query_double_list:
        val = ""
        for j in i[0:4]:
            if j == "-":
                continue
            else:
                val += info_dict[j]
        query_val.append([val, int(i[4])])

    # 점수 조건 먼저 확인: 이진탐색으로 조건 만족하는 인덱스 최솟값 찾기 
    result = []
    for s in query_val:
        q_score = s[1]
        q_info = s[0]

        if q_score > info_val[-1][1]:
            result.append(0)

        else:
            init = 0
            end = len(info_val) - 1

            while init < end:
                index = (init + end) // 2

                if q_score <= info_val[index][1]:
                    end = index
                else:
                    init = index + 1
            init_index = init

            # info조건 충족여부 판단 
            n = len(q_info)
            count = 0
            for i in range(init_index, len(info_val)):
                infos = info_val[i][0]

                if n == 8:
                    if q_info == infos:
                        count += 1
                elif n == 6:
                    if q_info[0:2] in infos and q_info[2:4] in infos and q_info[4:6] in infos:
                        count += 1

                elif n == 4:
                     if q_info[0:2] in infos and q_info[2:4] in infos:
                        count += 1
                elif n == 2:
                    if q_info[0:2] in infos:
                        count += 1
                else:
                    count += 1

            result.append(count)
            
    return result

