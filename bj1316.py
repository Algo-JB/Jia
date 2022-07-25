n = int(input())
cnt = 0

for i in range(n):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] != word[j+1]:
            chk = word[j+1:]
            if word[j] in chk:
                cnt -= 1
                break
    cnt += 1
print(cnt)
