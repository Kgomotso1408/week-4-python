file = open("example.txt","+a")

file.write("the folder is now completed!")

#now we open the file
file = open("example.txt","+rt")
data = file.read()
print(data)

