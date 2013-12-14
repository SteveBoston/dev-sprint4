#Ch. 11
# Steve Gallagher


#11.9

# def histogram(li):
# 	d = dict()
# 	for c in li:
# 		if c not in d:
# 			d[c] = 1
# 		else:
# 			d[c] = d[c] + 1
# 	return d

# def checker(d):
# 	for x in d:
# 		if d.get(x, 0) >= 2:
# 			return True				
# 	return False

# def has_duplicates(li):
# 	d = histogram(li)
# 	return checker(d)



# u = ["pie", "cake", "candy", "pie"]

# print has_duplicates(u)


#11.10

fin = open('words.txt')

def rot_pair(string1):
	fin = open("words.txt")
	for line in fin:
		word = line.strip()
		if len(word) == len(string1):
			a = list(word)
			a.reverse()
			a ="".join(a)
			if a == string1:
				b = dict()
				b[string1] = word
				return b




def rot_pair_total():
	fin2 = open("words.txt")
	final_dict = dict()
	for line in fin2:
		g = line.strip()
		b = rot_pair(g)
		if b != None:
			final_dict.update(b)
			z = final_dict	
	return z
		
		
		 
	# return complete dictionary

# def iterater():
# 	for line in fin:
# 		g = line.strip
# 		print rot_pair(g)

# # print rot_pair("evil")

print rot_pair_total()
