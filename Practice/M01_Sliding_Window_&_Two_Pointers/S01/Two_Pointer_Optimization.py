'''
input : [12,45,63,20,96,25,10]
output : [12,20,96,10]
create an empty list(res)
Traverse array and check elements is even or odd
display res

arr = list(map(int, input("Enter elements: ").split()))
res = []
for ele in arr:
    if ele % 2 == 0:
        res.append(ele)
print(res)
'''
'''
arr =  list(map(int,input().split()))
i = 0 
for j in range(len(arr)):
    if arr[j] % 2 == 0:
        arr[i] = arr[j]
        i += 1
print(arr[:i])

input : python 
output : nohtyp

s = input()
li = list(s)
left, right = 0 , len(s)-1
while left < right:
    li[left] , li[right] = li[right] , li[left]
    left += 1
    right -= 1
print("".join(li))
'''