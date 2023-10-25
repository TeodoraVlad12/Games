def merge(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge(left)
        merge(right)

        i=j=k=0

        while i<len(left) and j<len(right):
            if left[i]< right[j]:
                arr[k] = left[i]
                k += 1
                i+=1
            else:
                arr[k] = right[j]
                k+=1
                j+=1

        while i<len(left):
            arr[k] = left[i]
            k += 1
            i += 1

        while j<len(right):
            arr[k] = right[j]
            k += 1
            j += 1
    return arr

lista = [2,5,6,1,0,8,3,7,8,2,3]
merge(lista)
print(lista)
tup=(8,9,7)

print(isinstance(tup, tuple))
x={'a': 1, 'b':1}
del x['b']
print(x)