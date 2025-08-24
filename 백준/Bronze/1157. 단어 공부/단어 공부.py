n=input()
alpa=[0]*26
n=n.upper()
for ch in n:
    index=(ord(ch)-ord('A'))
    alpa[index]+=1
a=max(alpa)
if alpa.count(a)>1:
    print("?")
else:
    max_index=alpa.index(a)
    result=chr(max_index+ord('A'))
    print(result)