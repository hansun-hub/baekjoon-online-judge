n=int(input())
for _ in range(n):
    alpa = [0]*26
    word = input()
    for i in word:
        if i.isalpha():
            index = ord(i)-ord('a')
            alpa[index]+=1

    max_val = max(alpa)
    if alpa.count(max_val) >1:
        print("?")
    else:
        max_index = alpa.index(max_val)
        print(chr(max_index+ord('a')))