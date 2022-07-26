import os
import os

path = os.getcwd()
print("'"+path+"'")
aswr = input("Wanne use the current directory?[y / n]:")

if not(aswr.upper() == 'Y'): 
	path = input("Input the directory path:")

	
print("--------")
print("Text files in '{}':".format(path))
files = os.listdir(path)
try:
	for file in files:
		if file.endswith(".txt"):
			#print(os.path.join(path,file))
			print(file)
except:
	print("Cannot seach the directory")

print("------------")
fileName = input("Choose the file:").rstrip()

try:
	fhandUpper = open(fileName)
except:
	print("Cannot open the file")
for line in fhandUpper:
	print(line.upper().rstrip())
fhandUpper.close()

