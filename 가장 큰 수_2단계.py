def solution(numbers):
    num_dict = {}
    for n in numbers:
        num = str(n)
        d = len(num)
        
        if d == 1:
            num = num * 3
        
        elif d == 2:
            if num[0] > num[1]:
                num = num + f"{num[1]}.5"
            elif num[0] < num[1]:
                num = num + f"{num[0]}.5"
            else:
                num = num + f"{num[0]}"
        elif d == 4:
            num = "0000"
        
        if num not in num_dict.keys():
            num_dict[num] = str(n)
        else:
            num_dict[num] += str(n)
    
    
    num_dict_sorted = dict(sorted(num_dict.items(), key=lambda x:x[0], reverse=True))
    answer = "".join(num_dict_sorted.values())
    
    return answer