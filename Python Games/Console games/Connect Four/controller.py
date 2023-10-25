command=input("Enter: ")
index=command.find(" ")
if index ==-1:
    print("invalid")
print(command[:index])
print(command[index:])
atr=command[index:].split(';')
for a in atr:
    print (a)

file=input("Enter file name: ")
fin=open(file, "wt")
fin.write("hfhfhf")