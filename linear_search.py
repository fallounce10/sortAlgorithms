def linear_search(a_list, num):
	for i in range(len(a_list)):
		if a_list[i] == num:
			return num
	return -1
