#exercise 2
file = "mbox-short.txt"

try:
	fhand = open(file)
except:
	print("could not open the file ;)")

print("Email Address")
addr= input(">")
#email = email.split()
#addr = email[1]


entrys=[]
for line in fhand:
	line = line.rstrip()
	if line.startswith("From")and len(line.split()) > 2:
		entrys.append(line)

#[print(x) for x in entrys]

addr_entrys=dict()
for i in entrys:
	words= i.split()
	if words[1]==addr:
		addr_entrys[words[2]] = words[4] #the day[2] and date [4]
print(addr_entrys)
fhand.close()
