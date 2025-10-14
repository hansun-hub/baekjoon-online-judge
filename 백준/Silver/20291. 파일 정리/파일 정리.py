n = int(input()) # 파일 개수 입력 
extensions = {} 

for _ in range(n): 
    filename = input().strip() 
    name, ext = filename.split('.') # 점(.)을 기준으로 분리 
    extensions[ext] = extensions.get(ext, 0) + 1 # 확장자 개수 세기 
    
# 사전순으로 정렬 후 출력 
for ext in sorted(extensions.keys()): 
    print(ext, extensions[ext])