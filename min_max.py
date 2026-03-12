def max(arr):
    i=0
    max=arr[0]
    for j in range(i+1,len(arr)):
        if max<=arr[j]:
            max=arr[j]
    return max
def min(arr):
    i=0
    min=arr[0]
    for j in range(i+1,len(arr)):
        if min>=arr[j]:
            min=arr[j]
    return min
arr=[2,6,5,8,4,200,1]
minimum=min(arr)
maximum=max(arr)
print("minimum value is: ",minimum)
print("maximum value is: ",maximum)