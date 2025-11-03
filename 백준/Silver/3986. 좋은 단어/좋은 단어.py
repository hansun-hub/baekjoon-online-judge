n=int(input())
count=0
for _ in range(n):
    stack=[]
    box = input()
    for i in box:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if not stack:
            count+=1
print(count)