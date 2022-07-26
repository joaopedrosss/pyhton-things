fname = input("file name:")
try: 
   open(fname)
except:
    print("Cannot open:",fname)
    exit()

fhand=open(fname,"w")
text = input("Text:")
text += "\n"
fhand.write(text)

fhand.close()

print(open(fname).read())