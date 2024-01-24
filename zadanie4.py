n = int(input())
i = 0
num = 1 
while i < n:
    i += 1
    for j in range(i):
        print(num, end = " ")
        num += 1 
        j += 1
    print()
