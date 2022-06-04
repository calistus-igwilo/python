# Baseball Game


def baseball_game(ops):
    '''
    You are keeping score for a baseball game with strange rules. 
    The game consists of several rounds, where the scores of past rounds 
    may affect future rounds' scores.

    At the beginning of the game, you start with an empty record. 
    You are given a list of strings ops, where ops[i] is the ith operation 
    you must apply to the record and is one of the following:

    An integer x - Record a new score of x.

    "+" - Record a new score that is the sum of the previous two scores. 
    It is guaranteed there will always be two previous scores.

    "D" - Record a new score that is double the previous score. 
    It is guaranteed there will always be a previous score.

    "C" - Invalidate the previous score, removing it from the record. 
    It is guaranteed there will always be a previous score.

    '''
    #ops = ["5", "2", "C", "D", "+"]
    result = []
    for n in ops:
        if n == "+":
            result.append(result[-1] + result[-2])
        elif n == "D":
            result.append(2 * result[-1])
        elif n == "C":
            result.pop()
        else:
            result.append(int(n))
    return sum(result)

print(baseball_game(["5", "2", "C", "D", "+"]))


