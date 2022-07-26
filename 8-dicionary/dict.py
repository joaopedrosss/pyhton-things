import time

fhander = open('words.txt')
aurelio= dict()
for i in fhander: 
	words=[]
	words.extend(i.split())
	#print(words)
	for l in words:
		aurelio[l]=''
while True:
	w = input("Word>")
	if(w==''):break

	st = time.time()
	print(w in aurelio)
	ft = time.time()
	et = ft - st
	print("time: {:.5f}".format(et*100))
	#print("time:",et)
	print('-------')
fhander.close()