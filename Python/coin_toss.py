import random

def toss(coin):

    attempt = 1
    heads = 0
    tails = 0
    result = ""
    result_string_complete = ""

    for x in range(1, coin):
        new_toss = random.randint(0,1)
        if new_toss == 1:
            heads += 1
            result = "heads"
            print "Attempt #", attempt_count, ": Throwing a coin... It's a ", result, "! Got ", heads, "head(s) so far and", tails, "tail(s) so far"
        else:
            tails += 1
            result = "tail"
            print "Attempt #", attempt_count, ": Throwing a coin... It's a ", result, "! Got ", heads, "head(s) so far and", tails, "tail(s) so far"
        attempt_count += 1
