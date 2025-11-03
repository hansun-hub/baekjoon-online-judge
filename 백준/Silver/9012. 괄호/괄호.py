n=int(input())
for _ in range(n) :
    stack = []
    box=input()
    for i in box:
        if i == '(':
            stack.append('(')
        elif i==')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')

