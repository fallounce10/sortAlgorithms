def binary_search(a_list, num):
	low = mid = 0
	high = len(a_list) - 1

	while low <= high:
		mid = (high + low) // 2
		if a_list[mid] < num:
			low = mod + 1
		elif a_list[mid] > num:
			high = mid - 1
		else:
			return mid
	return -1  
