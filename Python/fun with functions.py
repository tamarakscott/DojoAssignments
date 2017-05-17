#odd and even number
def odd_even(number):
    for number in range(0,100):
        if (number %2==0):
            print("Number is" , number,  "This is an even number")
        else:
            print("Number is" , number,  "This is an odd number")
#Multiply
def multiply(a,num):
    for x in range(len(a)):
        a[x]*= num
        return a
        a = [2,4,10,16]
        b=multiply(a,5)
        print b
#hacker
def layered_multiples(arr):
    x = layered_multiples(multiply([2,4,5],3))
    new_array=[]
    for x in array:
        arr1 = []
        for y in range(0,x):
            arr1.append(1)
            new_array.append(arr1)
print x
