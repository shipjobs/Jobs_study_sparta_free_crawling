f = open("test.txt", "w", encoding="utf-8")

#쓰기
for i in [1,2,3,4,5]:
    f.write(f"{i} 번째 줄이예요 \n")


#읽어 오기
with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print("출력 라인"  + line)

#닫기
f.close()
