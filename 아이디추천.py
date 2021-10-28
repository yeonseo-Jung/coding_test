def solution(new_id):

    new_id_arr = []
    i = 0
    for s in new_id:
        # 1단계
        s = s.lower()  
        # 2단계
        if s not in possible:
            i += 1
            continue
        # 3단계
        if new_id[i-1] == "." and new_id[i] == ".":
            i += 1
            continue
                
        new_id_arr.append(s)
        i += 1
    
    # 4단계
    while new_id_arr[0] == ".":
        del new_id_arr[0]
    while new_id_arr[-1] == ".":
        del new_id_arr[-1]    
        
    # 5단계            
    if len(new_id_arr) == 0:
        new_id_arr.append("a")
    # 6단계    
    if len(new_id_arr) >= 16:
        new_id_arr = new_id_arr[0:16]
        while new_id_arr[-1] == ".":
            del new_id_arr[-1]
    # 7단계
    while len(new_id_arr) <= 2:
        new_id_arr.append(new_id_arr[-1])
    
    answer = ''.join(new_id_arr)
    return answer