x = open("pythontestfile.txt", "w") # w = write (Craeted a file that didn't exist before)
x.write("File created by pythonwrite.py")
x.close()
x = open("pythontestfile.txt", "r") #reads 'File created by pythonwrite.py'

x = open("pythontestfile.txt","a")
x.write("\nThis is the second line. Didn't exist before.")
x.close()