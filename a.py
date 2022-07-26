#exercise 5
print("text file name:")
file = input(">")
#file = 'mbox-short.txt'
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

domain_freq = dict()

for i in entrys:
	email = '' 
	addr= i.split()
	email += addr[1]
	
	domain = email[email.find('@'):]

	domain_freq[domain] = domain_freq.get(domain,0)+1

print(domain_freq)

fhand.close()
