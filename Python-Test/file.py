#for read

f = open("C:\\Users\HP\Desktop\Imp\demo.txt","r")
print(f.read())         #it will read the complete file
print(f.read(5))        #it will read based on alphabets
print(f.readline())     #it will read one line
print(f.readlines())    #it will read all the lines

#for write

f = open("C:\\Users\HP\Desktop\Imp\demo.txt","w")
f.write("My demo")
f.close()
f = open("C:\\Users\HP\Desktop\Imp\demo.txt","r")
print(f.read())

f = open("myfile.txt", "x")   #for create file

#for delete file
import os
os.remove("demofile.txt") # remove file
os.rmdir("myfolder")    # remove folder
