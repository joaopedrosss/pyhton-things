#exercise 3 and 4
print("text file name:")
file = input(">")

try:
	fhand = open(file)
except:
	print("could not open the file ;)")

entrys=[]
for line in fhand:
	line = line.rstrip()
	if line.startswith("From") and len(line.split())>2:
		entrys.append(line)

#[print(x) for x in entrys]
addr_freq = dict()
for i in entrys:
	i=i.split()
	addr=i[1]
	addr_freq[addr] = addr_freq.get(addr,0)+1

print(addr_freq)

emails=[]
emails.extend(addr_freq.keys())
big = 0
big_index = 0

for i in range(len(emails)):
	ad = emails[i]
	if addr_freq[ad] > big:
		big_index = i
		big = addr_freq[ad]

print(emails[big_index], big)

fhand.close()
