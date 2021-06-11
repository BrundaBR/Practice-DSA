def reverse(s):
	item=[]
	result=""
	for i in s:
		item.append(i)
	while len(item)>0:
		result+=item.pop()
	return result


print(reverse("HELLO"))

