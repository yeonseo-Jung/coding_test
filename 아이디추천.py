def solution(new_id):

    possible = "abcdefghijklmnopqrstuvwxyz-_.0123456789"

    new_id_arr = []
    new_id_str = ""
    # 1단계
    for s in new_id:
        # 1단계
        s = s.lower()
        # 2단계
        if s in possible:
            new_id_str += s
    # 3단계
    i = 0
    for s in new_id_str:
        if new_id_str[i-1] == "." and new_id_str[i] == ".":
            i += 1
            continue
        else:    
            new_id_arr.append(s)
            i += 1
    
    # 4단계
    while len(new_id_arr) != 0 and new_id_arr[0] == ".":
        del new_id_arr[0]
    while len(new_id_arr) != 0 and new_id_arr[-1] == ".":
        del new_id_arr[-1]    
    
    print(new_id_arr)
    # 5단계            
    if len(new_id_arr) == 0:
        new_id_arr.append("a")
    # 6단계    
    if len(new_id_arr) >= 16:
        new_id_arr = new_id_arr[0:15]
        while new_id_arr[-1] == ".":
            del new_id_arr[-1]
    # 7단계
    while len(new_id_arr) <= 2:
        new_id_arr.append(new_id_arr[-1])
    
    answer = ''.join(new_id_arr)
    return answer