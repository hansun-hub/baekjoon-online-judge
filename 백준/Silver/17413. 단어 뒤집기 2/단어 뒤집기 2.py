
s=input()

result = []
word = []
in_tag = False

for ch in s:
    if ch == '<':
        if word:
            result.extend(word[::-1])
            word = []
        in_tag = True
        result.append(ch)
    elif ch == '>':
        in_tag=False
        result.append(ch)
    elif in_tag:
        result.append(ch)
    elif ch == ' ':
        result.extend(word[::-1])
        word = []
        result.append(ch)
    else:
        word.append(ch)

if word:
    result.extend(word[::-1])

print("".join(result))
