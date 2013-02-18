f1 = file('plaintexts-binary.txt', 'r')
f2 = file('ciphertexts-binary.txt', 'r')
plain = f1.readlines()
cipher = f2.readlines()
f1.close()
f2.close()


def rbin(x,le):
	rlt = bin(x)[2:]
	if len(rlt)<le:
		rlt = (le-len(rlt))*'0'+rlt
	return rlt


	
k1 = '0111'
k2 = '0110'

s_i = range(2**16)
s_o = [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7]

s_box = dict([(rbin(x,4),rbin(y,4)) for x,y in zip(s_o,s_i)])
rlt = 0
f = file('4c', 'w')

l = [rbin(x,16) for x in range(2**15,2**16)]
maxi = 0
for j in l:
	for i in range(len(cipher)):
		v1 = reduce(lambda x,y:str(x)+str(y),[(int(x)+int(y))%2 for x,y in zip(j[0:4],cipher[i][0:4])])
		v2 = reduce(lambda x,y:str(x)+str(y),[(int(x)+int(y))%2 for x,y in zip(j[4:8],cipher[i][4:8])])
		v3 = reduce(lambda x,y:str(x)+str(y),[(int(x)+int(y))%2 for x,y in zip(j[8:12],cipher[i][8:12])])
		v4 = reduce(lambda x,y:str(x)+str(y),[(int(x)+int(y))%2 for x,y in zip(j[12:16],cipher[i][12:16])])
		u42 = s_box[v1][1]
		u46 = s_box[v2][1]
		u410 = s_box[v3][1]
		u414 = s_box[v4][1]
	#	f.write('U:(%s ,%s, %s, %s) P:(%s, %s, %s)\n'%(u46, u48, u414, u416, plain[i][4], plain[i][6], plain[i][7]))
		
		rlt += (int(u42)+int(u46)+int(u410)+int(u414)+int(plain[i][0])+int(plain[i][3])+int(plain[i][8])+int(plain[i][11]))%2
	if abs(rlt) > maxi:
		maxi = max(rlt, maxi)
		print "K5: %s, bias: %f"%(j,(rlt-5000)/float(10000))
		f.write("K5: %s, bias: %f"%(j,(rlt-5000)/float(10000)))
	rlt = 0
f.close()