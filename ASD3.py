def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]

		mergeSort(L)
		mergeSort(R)

		i = j = k = 0

		while i < len(L) and j < len(R):
			if L[i] >= R[j]: #Descending
			# if L[i] <= R[j]: #Ascending
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()



arr = [5, 2, 4, 7, 1, 3, 2, 6] #int
# arr = ["Vera", "Fauzan", "Novan", "Novi"] #string
print("Array sebelum sorting :")
printList(arr)
mergeSort(arr)
print("\nArray setelah sorting : ")
printList(arr)