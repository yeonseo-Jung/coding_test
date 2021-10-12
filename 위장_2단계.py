def combination(arr, r):
    if r == 0:
        return [[]]
    
    comb_arr = []
    i = 0
    for s in arr:
        rem_arr = arr[i + 1:]
        i += 1
        
        for p in combination(rem_arr, r-1):
            comb_arr.append([s] + p)
    
    return comb_arr

def solution(clothes): 
    clothes_dict = {}
    clothes_key = []
    for s in clothes:
        key = s[1]
        val = s[0]
        if not key in clothes_key:
            clothes_key.append(key)
            clothes_dict[key] = [val]
        else:
            clothes_dict[key].append(val)
    
    n = len(clothes_key)
    answer = 0
    for i in range(1, n+1):
        comb = combination(clothes_key, i)
            
        for l in comb:
            c = 1
            for k in l:
                c = c * len(clothes_dict[k])
            answer += c
            
    return answer