'''
approach1- remove 0's append at end
-run for loop 
-pop 0 append at end

'''




a=[1,2,0,0,3,4]
for i in a:
	if i == 0:
		a.remove(0)
		a.append(0)
print(a)

