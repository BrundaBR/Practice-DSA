def fun(h,n):
	if h=="" and n=="":
		return 0
	else:
		var_needle=n[0] # l
		for i in range(len(h)):
			if h[i]==var_needle:
				return i
			else:
				continue
		return -1



haystack = ""
needle = ""
print(fun(haystack,needle))


# "a" hay
# "" ned
# 0