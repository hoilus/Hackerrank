n = int(input().strip())
list = [int(x) for x in input().strip().split()]

list.sort()

index = int(n/2)
print(list[index])
