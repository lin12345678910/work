
dict1={"飢餓遊戲3":"在書架A的第1本","解憂雜貨店":"在書架A的第2本",
       "怪獸與牠們的產地":"在書架A的第3本","哈利波特6":"在書架A的第4本",
       "我的阿富汗筆友":"在書架A的第5本","祈念之樹":"在書架A的第6本",
       "樓下的房客":"在書架A的第7本","小王子":"在書架A的第8本",
       "房思琪的初戀樂園":"在書架B的第1本","等一個人的咖啡":"在書架B的第2本",
       "鬼滅之刃14":"在書架b的第3本","神農嘗百草":"在書架B的第4本",
       "麥田埔手":"在書架B的第5本","老人與海":"在書架B的第6本",
       "傲慢與偏見":"在書架B的第7本","與神同行":"在書架B的第8本"}
a=input("請輸入欲租借的書籍；")
if a in dict1:
    print(dict1[a])
else:
    print("查無此書籍")