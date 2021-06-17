a=b=1
c=int(input("請輸入正整數m的值："))
while(a<=c):
    b+=1
    a*=b
print("超過M為%d的最小階層N值為：%d" % (c,b))