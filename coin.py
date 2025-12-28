def coin(n):
    a = 0
    b = 0
    c = 0
    d = 0

    a = n//1000
    b = (n%1000)//500
    c = (n%500)//100
    d = (n%100)//10

    print("천원의 갯수 : " , a)
    print("오백원의 갯수 : " , b)
    print("백원의 갯수 : " , c)
    print("십원의 갯수 : " , d)

    return

n = 587951237
coin(n)
