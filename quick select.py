def particion(arreglo,l,r):
    pivot = arreglo[r]
    i = l

    for j in range(l,r):
        if arreglo[j] <= pivot:
            arreglo[i],arreglo[j] = arreglo[j],arreglo[i]
            i+=1
    arreglo[i],arreglo[r] = arreglo[r],arreglo[i]
    return i

def quickselect(arreglo, l, r, k):
    if(k > 0 and k<= r - l + 1):
        index = particion(arreglo,l,r)
        if (index - l == k - 1):
            return arreglo[index]
        if(index - l > k - 1):
            return quickselect(arreglo, l , index-1, k)
        return quickselect (arreglo,index+1,r,k-index+l-1)
    print("Index out of bound")

arr = [10, 4, 5, 8, 6, 11, 26]
n = len(arr)
k = 1
print("k esimo elemento mas pequeño del arreglo: ", end="")
print(quickselect(arr,0,n-1,k))