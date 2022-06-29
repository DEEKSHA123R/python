try:
    fileptr=open("D:\practicexy.txt")
except:
    print("pass")
else:
    print("fail")
finally:
    fileptr.close()


