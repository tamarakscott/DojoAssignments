import random
def score(grade):

    for count in range (0, grade):
        score = random.randint(60, 100)
    if score(score >59) and (score<=69):
        print score, "Your grade is D"
    elif (score >70) and (score<=79):
        print score, "Your grade is C"
    elif (score>80) and (score<=89):
        print score, "Your Grade is B"
    elif (score>90 )and (score<=100):
        print score,"Your grade is A"
    else:
        print "You failed"
        print "End of the program.  Bye!"
