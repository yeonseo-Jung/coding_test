# 최대 거리를 통해 세점의 중간 좌표 찾기 
# 중간좌표를 기준으로 벡터연산 통해 나머지 좌표찾기
d_max = max(d_arr)
i_max = d_arr.index(d_max)
if i_max == 0:    # 중간좌표 index = 2
    x = v[0][0] + v[1][0] - v[2][0]
    y = v[0][1] + v[1][1] - v[2][1]
elif i_max == 1:    # 중간좌표 index = 0
    x = v[1][0] + v[2][0] - v[0][0]
    y = v[1][1] + v[2][1] - v[0][1]
elif i_max == 2:    # 중간좌표 index = 1
    x = v[0][0] + v[2][0] - v[1][0]
    y = v[0][1] + v[2][1] - v[1][1]

answer = [x, y]