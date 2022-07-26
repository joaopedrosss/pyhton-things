def invalid():
	print("Invalid input")
	exit()	

name = input("Nome:")
sex = input("Sexo [M]/[F]:")
gender = sex.upper()

if not(gender=="M" or gender=="F"):
	invalid()

fhander = open("total-people.txt","a")
fhander.write(name+" "+gender+"\n")
fhander.close()

print("----------------")

fwrite = open("total-people.txt","r")
population = [];
for line in fwrite:
	print(line.rstrip())
	data = line.split()
	population.append(data)

males = 0
females = 0
for i in population:
	#print(i)
	if(i[1] == "F"):
		females+=1
	else:
		males+=1
print("----------------")
print("Males:{}\nFemales:{}".format(males,females))

total = males + females;

if(gender=="M"):
	print("You {} are part of the {:.0%} of the population".format(name,males/total))
else:
	print("You {} are part of the {:.0%} of the population".format(name,females/total))	

fwrite.close()	
