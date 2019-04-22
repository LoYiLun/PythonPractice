import os
print("please input dataPath")
dirPath = "C:/Users/user/Desktop/新增資料夾/ADT104101"
#os.chdir(dirPath)

print("please input data name")
dirName = str(input())

print("please input data number(begin)")
indexB = int(input())

print("please input data number(end)")
indexE = int(input())

for i in range(indexB,indexE+1):
    if(i < 10):
        fp = open(dirName + '0' +str(i) + '.docx',mode='w')
        fp.close()
    else:   
        fp = open(dirName +str(i) + '.docx')
        fp.close()
