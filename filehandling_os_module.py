import os

# to check the current working directory
print(os.getcwd())

#to change the directory
os.chdir(r"C:\Users\User\OneDrive\Desktop\svit")
print(os.getcwd())

#to create a directory
#os.mkdir("example") #if the folder already exist itb will throw u FileExistError
#to remove the directory
#os.rmdir("example")
#os.mkdir("example")
os.chdir(r"C:\Users\User\OneDrive\Desktop\svit\example")
#os.mkdir("sample.py")
#os.mkdir("sample2.txt")
#os.rmdir("sample.py")
#os.mkdir("overriding_class_variable.py")
path1 = r"C:\Users\User\OneDrive\Desktop\svit"
#os.chdir(r"C:\Users\User\OneDrive\Desktop\svit")
#print(os.listdir())
print(os.path.exists(path1))
print(os.path.getsize(path1))






