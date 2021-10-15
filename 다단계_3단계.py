# 3차 시도
def solution(enroll, referral, seller, amount):    
    # seller 배열에서 중복 제거하기 
    # -> key: seller 이름, value: 한번의 판매량을 원소로 하는 리스트인 딕셔너리 생성
    seller_dict = {}
    i = 0
    for s in seller:
        if s in seller_dict.keys():
            seller_dict[s].append(amount[i])
        else:
            seller_dict[s] = []
            seller_dict[s].append(amount[i])
        i += 1

    # seller의 추천인들 찾기
    recommender = []
    i = 0
    for s in seller_dict.keys():
        index = enroll.index(s)
        recommender.append([index])
        while referral[index] != "-":
            index = enroll.index(referral[index])
            recommender[i].append(index)
        i += 1

    # 이익 분배하기
    result = [0] * len(enroll)
    i = 0
    for s in seller_dict.keys():
        for a in seller_dict[s]:
            p = a * 100
            for j in recommender[i]:
                if p < 1:
                    break
                elif j == recommender[-1]:
                    result[j] += p 
                else:
                    result[j] += p - p // 10
                    p = p // 10
        i += 1

    return result