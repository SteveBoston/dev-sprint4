#Steve Gallagher Chapter 11

fin = open('words.txt')

# fin1 = list(fin)

# f = []

# for x in fin1:
# 	x = x.strip()
# 	f.append(x)






#This is a change

# #10.7

# def is_anagram(string1, string2):
# 	a = list(string1)
# 	b = list(string2)

# 	a.sort()
# 	b.sort()

# 	n = 0

# 	def checker(a,b,n):
# 		if n < len(a) and a[n] == b[n]:           
# 			n = n + 1
# 			return checker(a,b,n)

# 		elif n < len(a) and a[n] != b[n]:
# 			print "No, these words are not anagrams."
# 			return False

# 		elif n >= len(a):
# 			print "Yes, these words are anagrams."
# 			return True
		

		

# 	if len(a) == len(b):
# 		return checker(a,b,n)


# 	else:
# 		print "No, these words are not anagrams."
# 		return False
	



# print is_anagram("reeh", "here")





#10.13 interlocking words

def interlock(a,b,c,n):
	for x in a:
		c.append(a[n])
		c.append(b[n])
		n = n + 1
	delimeter = ""
	d = delimeter.join(c)
	e = d.strip()
	return e

		
		


def interlock_check(string1):
	fin1 = open('words.txt')
	for line in fin1:
		word = line.strip()
		if len(string1) == len(word):
			a = string1
			b = word
			n = 0
			c = []
			e = interlock(a,b,c,n)
			fin2 = open('words.txt')
			for line in fin2:
				word = line.strip()
				if e == word:
					print e
	print "done with word"


def interlock_total():
	fin3 = open('words.txt')
	for line in fin3:
		word = line.strip()
		interlock_check(word)




interlock_total()




