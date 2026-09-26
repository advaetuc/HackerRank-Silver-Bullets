a = int(input())
b = int(input())
m = int(input())

if 1 <= a <= 100 and 1 <= b <= 100 and 2 <= m <= 1000:
    print(pow(a,b))
    print(pow(a,b,m))
