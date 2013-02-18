f1 = file('plaintexts-binary.txt', 'r')
f2 = file('ciphertexts-binary.txt', 'r')
plain = f1.readlines()
cipher = f2.readlines()
f1.close()
f2.close()

s_i = range(2**16)
s_o = [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7]

s_box = dict([(x,y) for x,y in zip(s_o,s_i)])
rlt = 0
f = file('4c', 'w')

l = ['{0:016b}'.format(x) for x in range(2**15,2**16)]
maxi = 0
for j in l:
	for i in range(len(cipher)):
		v1 = int(j[0:4],2) ^ int(cipher[i][0:4],2)
		v2 = int(j[4:8],2) ^ int(cipher[i][4:8],2)
		v3 = int(j[8:12],2) ^ int(cipher[i][8:12],2)
		v4 = int(j[12:16],2) ^ int(cipher[i][12:16],2)
		u42 = '{0:04b}'.format(s_box[v1])[1]
		u46 = '{0:04b}'.format(s_box[v2])[1]
		u410 = '{0:04b}'.format(s_box[v3])[1]
		u414 = '{0:04b}'.format(s_box[v4])[1]
	#	f.write('U:(%s ,%s, %s, %s) P:(%s, %s, %s)\n'%(u46, u48, u414, u416, plain[i][4], plain[i][6], plain[i][7]))
		rlt += (int(u42)+int(u46)+int(u410)+int(u414)+int(plain[i][0])+int(plain[i][3])+int(plain[i][8])+int(plain[i][11]))%2
	if abs(rlt) > maxi:
		maxi = max(rlt, maxi)
		print "K5: %s, bias: %f"%(j,(rlt-5000)/float(10000))
		f.write("K5: %s, bias: %f"%(j,(rlt-5000)/float(10000)))
	rlt = 0
f.close()