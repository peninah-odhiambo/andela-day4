def find_missing (list1, list2):
	""" The lists represent two different lists"""

	# list1 = set (list1)
	# list2 = set (list2)
	if len(list1) > len(list2):
		for number in list1:
			if number not in list2:
				return number
	else:
		for number in list2:
			if number not in list1:
				return number
	"""set gets rids of duplicates in the lists"""		
			


print(find_missing([1,2,2,3,4], [1,2,3,4,5]))