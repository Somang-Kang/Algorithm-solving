import itertools

num = int(input())
answer = []
for i in range(1,11):
    for j in itertools.combinations(range(10),i):
        str_num = ''.join(list(map(str,reversed(list(j)))))
        answer.append(int(str_num))
answer = sorted(answer)

if num>=len(answer):
    print(-1)
else:
    print(answer[num])