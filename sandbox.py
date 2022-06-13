from itertools import count


first, *last = [1, 2, 3, 4, 5, 6, 7]
print("first: ", first)
#print("second: ", second)
print("last: ", last)

word = 'letters in deo'
print(word.count('t'))

# from collections import Counter
# def solution(cards):
#     highest =[]
#     count = []
#     for item in cards:
#         highest.append(max(item))
#     for item in highest:
#         for i in cards:
#             if highest[item] in cards[i]:
#                 count.append(item)
#     max_list = Counter(count)
#     return max_list

input_cards = [[5,7,3,9,4,9,8,3,1], [1,2,2,4,4,1], [1,2,3]]
#print(solution(input_cards))
def solution(cards):
    max_nums = [max(num) for num in input_cards]
    print(max_nums)
    cnt = []
    for num in max_nums:
        for i in range(len(input_cards)):
            if num in input_cards[i]:
                cnt.append(num)
    res = [num for num in cnt if cnt.count(num)==1]
    if len(res) == 1:
        return res
    else:
        return -1


def draw_rating(vote):
    # Write your code here...
    if vote >= 0 and vote <= 20:
        df.assign(Rating=df['Rating'].apply(lambda x: x * '*') )
    elif vote > 20 and vote <= 40:
        df.assign(Rating=df['Rating'].apply(lambda x: x * '**') )