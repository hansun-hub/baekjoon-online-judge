
name = input().strip()

#에러체크
if name[0]=='_' or name[-1] =='_' or '__' in name:
    print("Error!")
elif '_' in name and any(ch.isupper() for ch in name):
    print("Error!")
elif '_' in name: #C++ -> Java
    parts = name.split('_')
    if any(p=='' for p in parts):
        print("Error!")
    else:
        result = parts[0] + ''.join(p.capitalize() for p in parts[1:])
        print(result)
elif any(ch.isupper() for ch in name): # java -> C++
    if not name[0].islower():
        print("Error!")
    else:
        result = ''
        for ch in name:
            if ch.isupper():
                result +='_' + ch.lower()
            else:
                result+=ch
        print(result)
else:
    print(name)
    