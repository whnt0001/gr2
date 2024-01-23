from random import randint

a = [10, 14, 11, 1, 124, 53, 534, 656, 7, 56]
N = len(a)

for i in range(N-1):
    for j in range(N-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
 
print(a)