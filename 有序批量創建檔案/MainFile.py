import os
print("please input dataPath")
dirPath = input()
os.chdir(dirPath)

print("please input data name")
dirName = str(input())

print("please input Filename Extension(副檔名)")
Filename = str(input())

print("please input data number(begin)")
indexB = int(input())

print("please input data number(end)")
indexE = int(input())

for i in range(indexB,indexE+1):
    if(i < 10):
        fp = open(dirPath + '/' + dirName + '0' +str(i) + '.' + Filename,mode = 'w')
    else:   
        fp = open(dirPath + '/' +dirName +str(i) + '.' + Filename,mode = 'w')
