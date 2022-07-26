#word counter
import time
import string

file = input(">File name (txt file):")
try:
	text = open(file)
except:
	print("could not open "+file)

d = dict()

st = time.time()
for line in text:

	#formatation
	line = line.translate(line.maketrans("","",string.punctuation))
	line=line.lower()

	for w in line.split(): 
		d[w] = d.get(w,0)+1
ft = time.time()

alfa=[]
alfa.extend(d.keys())
alfa.sort(key=str.lower)
for i in alfa:
	print("{} - {} times".format(i, d[i]))

#print("Time: ",st,"-",ft)

text.close()