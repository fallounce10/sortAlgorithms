def bubble_sort(a_list):
	for i in range(len(a_list) - 1):
		for j in range(len(a_list) - 1):
			if a_list[j] > a_list[j+1]:
				temp = a_list[j]
				a_list[j] = a_list[j+1]
				a_list[j+1] = temp

	return a_list
