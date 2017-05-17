man = ['magical unicorns',19,'hello',98.98,'world']

isMixed = False
firstType = type(man[0])
sum = 0
listSize = 0
myString = ""
for count in range(0, len(man)):
    if type(man[count]) != firstType:
        isMixed = True
    if type(man[count]) == int:
        sum += man[count]
    elif type(man[count]) == str:
        myString += " " + man[count]
    elif type(man[count]) == list:
        listSize += len(man[count])
if isMixed:
    print "The array you entered is of mixed type"
    print "String: " + myString
    print "Sum: " + str(sum)
    if listSize > 0:
        print "The total number of list items is: " + str(listSize)
elif isMixed == False:
     if firstType == int:
         print '"The array you entered is of int type"'
         print "Sum: " + str(sum)
     elif firstType == str:
         print '"The array you entered is of String type"'
         print "String: " + myString
     elif firstType == list:
         print '"The array you entered is of List type"'
         print "The total number of list items is: " + str(listSize)
