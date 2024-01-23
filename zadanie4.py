n = int(input())
i = 1
j = 1
cnt = 1
num = 1
while i <= n:
    i  += 1
    while j <= cnt:
        print(num, end = ' ')
        num += 1
        j += 1
    print()
    cnt +=1
