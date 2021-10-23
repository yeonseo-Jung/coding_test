import pandas as pd

def combination(arr, n):
    if n == 0:
        return [[]]
    
    result = []
    for i in range(len(arr)):
        m = arr[i]
        rList = arr[i + 1:]
        for s in combination(rList, n-1):
            result.append([m] + s)
            
    return result

def solution(info, query):
    # 배열 info를 정보별로 분류해서 list에 할당
    infoList = []
    for s in info:
        s = s.split()
        score = int(s.pop())
        s.append(score)
        infoList.append(s)
    # 분류된 배열 info_list를 DataFrame에 할당
    infoData = pd.DataFrame(infoList, columns=["0", "1", "2", "3", "Score"])
    # Score columns를 기준 오름차순으로 정렬
    infoData = infoData.sort_values(by="Score").reset_index(drop=True)
    # score list 생성
    scoreList = list(infoData["Score"])

    arr = ['0', '1', '2', '3']
    combList = []
    for i in range(1, 5):
        combList += combination(arr, i)

    infoData_16 = pd.DataFrame()
    for a in combList:
        s = ''.join(a)
        empty_str = [""] * len(scoreList)
        infoSeries = pd.Series(empty_str)
        for i in a:
            infoSeries += infoData.loc[:, i]
        infoData_16[f'{s}'] = infoSeries
    infoData_16['Score'] = scoreList

    result = []
    for q in query:
        # query 배열에서 필요한 정보 추출하기
        queries = q.replace("and ", "").split(" ")
        infos = ""
        q_info = ""
        for i in range(len(queries) - 1):
            if queries[i] == "-":
                continue
            else:
                infos += f'{i}'
                q_info += queries[i]
        q_score = int(queries[-1])

        # score 조건 충족하는 info_data의 index 최솟값 찾기
        if q_score > scoreList[-1]:
            result.append(0)
            continue
        else:
            # lower bound binary search 
            init = 0
            end = len(scoreList) - 1
            while init < end:
                index = (init + end) // 2
                if q_score <= scoreList[index]:
                    end = index
                else:
                    init = index + 1
            init_index = init

        if infos == "":
            n = len(scoreList) - init_index
            result.append(n)
        else:
            l = list(infoData_16.loc[init_index:, infos])
            n = l.count(q_info)
            result.append(n)
        
    return result