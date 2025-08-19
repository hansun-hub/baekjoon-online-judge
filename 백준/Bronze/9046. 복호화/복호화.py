n=int(input())

for _ in range(n) :
    counts = [0] * 26
    blnk = input()

    for ch in blnk:
        if ch.isalpha():
            counts[ord(ch)-ord('a')]+=1

    max_val = max(counts)

    if counts.count(max_val) > 1:
        print("?")
    else:
        max_idx = counts.index(max_val)
        print(chr(max_idx+ord('a')))