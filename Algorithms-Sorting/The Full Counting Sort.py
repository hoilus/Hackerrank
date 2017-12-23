def countingSort(mylist):
    num_list = [x[0] for x in mylist]
    str_list = [x[1] for x in mylist]
    # find the length, max and min of the input list
    L = len(num_list)
    max_list = max(num_list)
    min_list = min(num_list)
    
    # creating a count list with initial values as zero
    # creating a list to store the corresponding switched strings
    countList = [0 for i in range(min_list, max_list+1)]
    strList = len(countList)*['']
    
    # counting number of times each element occurs in the list and storing the count in the coutList
    # update the strList
    for element in mylist:
        countList[element[0] - min_list] += 1
        strList[element[0] - min_list] += element[1]+' '
    
    # starting from the min element to max element
    # inserting values according to their counting numbers in the new list in sorted order
    # inserting the sorted string list as well
    element = min_list
    num_list.clear()
    sorted_str = []
    for Count in countList:
        num_list += [element for i in range(Count)]
        sorted_str.append(strList[element-min_list])
        element += 1
        
    return sorted_str


n = int(input().strip())
mylist = [[0 for x in range(2)] for x in range(n)]

for i in range(n):
    numX, strX = input().strip().split()
    if i < n // 2:
        mylist[i][0] = int(numX)
        mylist[i][1] = '-'
    else:
        mylist[i][0] = int(numX)
        mylist[i][1] = strX

str_list = countingSort(mylist)
print(''.join(x for x in str_list))
#print(mylist)
#print([x[0] for x in mylist])
