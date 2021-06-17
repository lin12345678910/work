dict1={"蘋果":"紅色","香蕉":"黃色","葡萄":"紫色","藍莓":"藍色","橘子":"橘色"}
print(dict1.keys())
a=input("請輸入水果：")
if a not in dict1:       
    print("沒有%s這個水果" % (a))
    data1=input("請輸入水果：")
else:
    print(a+"是"+dict1[a])