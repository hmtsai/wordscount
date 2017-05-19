import sys

def tp2(t):
	return t[1]	# return 2nd item in tuple

def tp1(t):
	return t[0]	# return first item tuple

def is_key_exist(key, d):
	return True if key in d.keys() else False

def wc(fn):
	d = {}	# dictionary key:value would be tuple of (str, num) 

	f = open(fn, mode='r')
	for ln in f:
		#print(ln)
		lst = ln.split()
		for word in lst:
			if is_key_exist(word, d):
				d[word] += 1
			else:
				d[word] = 1

	for itm in sorted(d.items(), key=tp2):	# d.items() is a list of tuples, sort the tuples by 2nd element of tuple, key function point to tp2
		print(itm)

		


def main():
	wc(sys.argv[1])

if __name__ == '__main__':
	main()
