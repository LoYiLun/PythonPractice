import os
print("please input dataPath")
dirPath = str(input())
os.chdir(dirPath)

print("please input data name")
dirName = str(input())

print("please input data number(begin)")
indexB = int(input())

print("please input data number(end)")
indexE = int(input())

for i in range(indexB,indexE+1):
    if(i < 10):
        os.mkdir(dirName + '0' +str(i))
        
    else:   
        os.mkdir(dirName + str(i))
        
