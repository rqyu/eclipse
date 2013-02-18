import sys

filename = sys.argv[1]

def fetch_between(string, del1, del2):
	s = ""
	flg1 = 0
	for i in string:
		if i == del1:
			flg1 = 1
		if flg1==1 and i == del2:
			return s
		if flg1 == 1:
			s = s + i
	return ""
