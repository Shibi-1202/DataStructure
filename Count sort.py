def countsort(arr):
    count=[0]*10
    result=[0]*len(arr)
    for i in range(0,len(arr)):
        count[arr[i]]+=1
    for i in range(1,10):
        count[i]+=count[i-1]
    for i in range(len(arr)-1,-1,-1):
        result[count[arr[i]]-1]=arr[i]
        count[arr[i]]-=1
    for i in range(0,len(arr)):
        arr[i]=result[i]
arr=list(map(int,input("Enter the element with separated space: ").split()))
countsort(arr)
for i in range(0,len(arr)):
    print(arr[i],end=' ')
    
