def Solution(n):

    length = len(number)
    length = length - 4
    for i in range (length):
        print("*",end=' ')
    
    for i in range (4):
        print(number[length + i],end=' ')

    return

number = '01020171217'
Solution(number)