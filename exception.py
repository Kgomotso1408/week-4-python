file = input("Enter the filename:")
print("The filename is :"+file)

try:
    with open("file","r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("the file does not exist")
except Exception as e:
    print("an error occurred: ",e)    