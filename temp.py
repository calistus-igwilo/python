S = "111222311"
def compress_string(S):
    result = []
    temp = []
    i = 0
    cnt = 0
    j = i + 1


    if len(S) == 0:
        return "string must contain at least 1 element"
    while i <= len(S)-1:
        temp.append(S[i])
        cnt += 1    
        while  S[i] == S[j]:
            temp.append(S[i])
            cnt += 1
            i += 1
            j += 1
            print(f'i: {i}')
            print(f'j: {j}')
            print(f'cnt: {cnt}')
        
        result.append((cnt, temp[-1]))
        print(f'Layer 2 i: {i}')
        print(f'Layer 2 j: {j}')

        #temp = []
        
    return result

compress_string(S)