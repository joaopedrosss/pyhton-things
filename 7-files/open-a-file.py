import os

def printTextFiles(path):
	for file in os.listdir(path):
		if file.endswith(".py"):
			print(file)

print("-----------")
path = os.getcwd()
print("Text files in '{}:'".format(path))
printTextFiles(path)
print("-----------")

fname = input("File name:")
try:
	fhander = open(fname)
except:
	print("File cannot be opened: ",fname)
	exit()

keyWord = input("Show if it starts with:")#X-DSPAM-Confidence
count=0
for line in fhander:
	if(line.startswith(keyWord)):
		line = line.rstrip()
		print(line)
	count+=1


print("---TOTAl---")
print("Line count: {}".format(count))
fcontent = open(fname).read()
print("Word count: {}".format(len(fcontent)))


