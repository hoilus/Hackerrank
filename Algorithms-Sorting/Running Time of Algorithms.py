def insertion_sort(l):
    R = 0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
           R += 1
        l[j+1] = key
    return R

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
switchnum = insertion_sort(ar)
#print(" ".join(map(str,ar)))
print(switchnum)
