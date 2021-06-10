
'''
anagram is where rearrarging
a word is giving another word
'''




def check_for_anagram(s,t):
	n=len(s)
	m=len(t)
	s=sorted(list(s))
	t=sorted(list(t))
	if s==t:
		return True
	else:
		return False




s=input()
t=input()
print(check_for_anagram(s,t))