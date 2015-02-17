s = ""
for a in range(2000, 3201):
	if (a % 7 == 0) and not(a % 5 == 0):
		s = s + "," + str(a)
print s[1:]