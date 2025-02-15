def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
arr = list(map(int,input("Enter the element with separated space: ").split()))
x=int(input("Enter the search element: "))
result =search(arr,x)
if result!=-1:
    print(f"Element is present at index {result}")
else:
    print(f"Element is not present in the array")
