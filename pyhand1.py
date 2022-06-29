'''fileptr=open("D:\practicexy.txt","r")
fileptr.read()
if fileptr:
    print("open successfully")
else:
    print("not opened")
    fileptr.close()'''

with open("D:\practicexy.txt") as m:
    p=m.write("hello")
    m.read()
    print(p)

