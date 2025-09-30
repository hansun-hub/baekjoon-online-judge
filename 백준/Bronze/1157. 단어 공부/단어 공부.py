from collections import Counter

word = input().upper()
counter = Counter(word)

max_count = max(counter.values())
most_common = [ch for ch,cnt in counter.items() if cnt==max_count]

if len(most_common) > 1:
    print("?")
else:
    print(most_common[0])