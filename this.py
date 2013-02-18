import time
t = time.time()
f = file('crontest', 'a')
f.write(str(t)+'\n')
f.close()

