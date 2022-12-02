S = [1, 1, 1, 2, 2, 2, 3, 1, 1]
def compress_string(S):
    result = []
    temp = []
    repeat = []
  


    if len(S) == 0:
        return "string must contain at least 1 element"
    S = S[::-1]
    print("reverse", S)
    
    while len(S):
        temp.append(S.pop())
        while S[-1] == temp[-1]:
            temp.append(S.pop())
        result.append(temp[-1])
        repeat.append(len(temp))
        print(result)
        print(repeat)
        temp = []
    answer = dict(zip(result, repeat))
    print("numbe, repeat", answer)
        


compress_string(S)