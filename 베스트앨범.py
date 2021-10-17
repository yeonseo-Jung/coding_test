def solution(genres, plays):
    # 장르명을 key, [[고유번호, 재생횟수], ...]를 value로 하는 딕셔너리 
    plays_dict = {}
    i = 0
    for s in genres:
        if s in plays_dict.keys():
            plays_dict[s].append((i, plays[i]))
        else:
            plays_dict[s] = []
            plays_dict[s].append((i, plays[i]))
        i += 1
    # 한 장르 내에서 재생횟수를 기준으로 내림차순 정렬
    for s in plays_dict.keys():
        plays_dict[s] = sorted(plays_dict[s], key=lambda play: play[1], reverse=True)

    # 장르명을 key, 장르별 전체 재생횟수를 value로 하는 딕셔너리
    genres_dict = {}
    i = 0
    for s in genres:
        if s in genres_dict.keys():
            genres_dict[s] += plays[i]
        else:
            genres_dict[s] = plays[i]
        i += 1
    # 장르별 전체 재생횟수(value)를 기준으로 내림차순 정렬
    genres_dict = dict(sorted(genres_dict.items(), key=lambda item: item[1], reverse=True))

    # 재생횟수가 높은 장르를 순서로 장르내에서 재생횟수가 높은 두개 노래의 고유번호를 answer 리스트에 추가
    # 단, 장르안에 노래가 한개라면 한개만 리스트에 추가 
    answer = []
    for s in genres_dict.keys():
        if len(plays_dict[s]) == 1:
            song_num = plays_dict[s][0][0]
            answer.append(song_num)
        else:
            song_num_0 = plays_dict[s][0][0]
            song_num_1 = plays_dict[s][1][0]
            answer.append(song_num_0)
            answer.append(song_num_1)   
    
    return answer