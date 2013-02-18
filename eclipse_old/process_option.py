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

def find_exp_date(string):
	s = ""
	for i in range(len(string)):
		if "expiry" in s:
			rlt = fetch_between(string[i:], '{','}')
			break
		s = s + string[i]
		
	rlt = rlt[1:]
	rlts = rlt.split(',')
	rlt = rlts[0].split(':')[1] + '-'
	
	months = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun'
	,7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
	
	rlt = rlt + months[int(rlts[1].split(':')[1])] + '-'
	rlt = rlt + rlts[2].split(':')[1]
	
	return rlt
	
def get_option(type,string):
	s = ""
	for i in range(len(string)):
		if type in s:
			rlt = fetch_between(string[i:], '[',']')
			break
		s = s + string[i]
		
	rlts = rlt.split('{')
	rlt = []
	for i in rlts:
		if 'cid' in i:
			a = i.split(',')
			r = {}
			for j in range(len(a)):
				if 'strike' in a[j]:
					r['strike'] = float(a[j].split(':')[1].strip('"'))
				if 'p:' in a[j]:
					if '-' not in a[j]:
						r['price'] = float(a[j].split(':')[1].strip('"'))
					else:
						r['price'] = 0
				if 'c:' in a[j]:
					if '-' not in a[j]:
						r['change'] = float(a[j].split(':')[1].strip('"'))
					else:
						r['change'] = 0
				if 'b:' in a[j]:
					if '-' not in a[j]:
						r['bid'] = float(a[j].split(':')[1].strip('"'))
					else:
						r['bid'] = 0
				if 'a:' in a[j]:
					if '-' not in a[j]:
						r['ask'] = float(a[j].split(':')[1].strip('"'))
					else:
						r['ask'] = 0
				if 'vol:' in a[j]:
					if '-' not in a[j]:
						r['volume'] = float(a[j].split(':')[1].strip('"'))
					else:
						r['volume'] = 0
				if 'oi:' in a[j]:
					if '-' not in a[j]:
						r['open int'] = float(a[j].split(':')[1].strip('"'))
					else:
						r['open int'] = 0
				if 'expiry:' in a[j]:
					r['exp'] = a[j].split(':')[1].strip('"')
			rlt.append(r)
	
	return rlt
	
def get_price(string):
	s = ""
	rlt = ''
	rlt = fetch_between(string, '>','<')
	return float(rlt[1:])
		
		
def get_tag_content(tag_name):
	f = open(filename, 'r')
	d = f.readlines()
	f.close()
	for i in range(len(d)):
		if "google.finance.data =" in d[i]:
			data = d[i]
		if 'class="pr bld">' in d[i]:
			pricing = d[i+1]
	
	s = find_exp_date(data)
	puts = get_option('put', data)
	calls = get_option('call', data)
	price = get_price(pricing)
	
	diff = float(puts[1]['strike']) - float(puts[0]['strike'])
	
	rlt = '<table style="font-family:verdana;font-size:14px">'
	rlt = rlt + '<tr><td>Current ' + tag_name[0:4] + ' Price</td><td style="font-family:verdana;color:red;font-size:20px">' + str(price) + '</td></tr>'
	rlt = rlt + '<tr><td>Puts</td></tr>'
	rlt = rlt + '<tr><td>Strike</td><td>Bid/Ask</td><td>Date</td></tr>'
	for i in puts:
		if abs(i['strike']-price) <= diff*2:
			rlt = rlt + '<tr><td>' + str(i['strike']) + '</td><td>'+ str(i['bid']) + '/' + str(i['ask']) + '</td><td>' + i['exp'] + '</td></tr>'
			
	rlt = rlt + '<tr></tr>'
	rlt = rlt + '<tr><td>Calls</td></tr>'
	rlt = rlt + '<tr><td>Strike</td><td>Bid/Ask</td><td>Date</td></tr>'
	for i in calls:
		if abs(i['strike']-price) <= diff*2:
			rlt = rlt + '<tr><td>' + str(i['strike']) + '</td><td>' + str(i['bid']) + '/' + str(i['ask']) + '</td><td>' + i['exp'] + '</td></tr>'
	rlt = rlt + '</table>'
	
	return rlt
	
def to_temp(string):
	f = open('temp.txt', 'w')
	f.write(string)
	f.close()
	
to_temp(get_tag_content(filename))