# 개수 세기
N = int(input())

n = list(map(int, input().split()))

v = int(input())
print(n.count(v))

#X보다 작은 수
N, X = map(int, input().split())
A = list(map(int, input().split())) #공백으로 구분된 N개의 숫자를 입력받아 정수리스트 A를 만듦

for i in range(N): #i를 0~N-1까지 반복
    if A[i] < X: #A[i] => 리스트의 i번째 원소가 기준값 X보다 작은지 비교
        print(A[i], end=" ") #조건을 통과한 값 A[i]를 한 줄에 공백으로 구분해 출력, end " "때문에 줄바꿈 대신 띄어쓰기 가능


#최대, 최소
N = int(input())
X = list(map(int, input().split()))
print(min(X), max(X), end = " ") #for함수가 필요없음.

#최댓값
numbers = []

for _ in range(9):
    i = int(input())
    numbers.append(i)

print(max(numbers))
print(numbers.index(max(numbers)) + 1)

#공넣기
N, M = map(int, input().split())

box = [0]*N

for m in range(M):
    i, j, k = map(int, input().split())
    for x in range(i, j+1):
        box[x-1] = k
for x in range(N):
    print(box[x], end = " ")

#공 바꾸기
N, M = map(int, input().split())

box = list(range(1, N+1))

for _ in range(M):
    i, j = map(int, input().split())
    box[i-1], box[j-1] = box[j-1], box[i-1]

print(*box)


#과제 안 내신 분..?
#import random

#n = list(range(1, 31))
#n_random = random.sample(n, 28)

#m_random = sorted(set(n) - set(n_random))
#print(m_random[0])
#print(m_random[1])

n = list(range(1, 31))

for _ in range(28):
    i = int(input())
    n.remove(i)

for j in n:
    print(j)

#나머지
numbers = []
for _ in range(10):
    i = int(input())
    numbers.append(i)

n_numbers = set() #set()은 중복을 허용하지 않는 집합

for num in numbers:
    n_numbers_1 = num % 42
    n_numbers.add(n_numbers_1)

print(len(n_numbers))

#바구니 뒤집기
N, M = map(int, input().split())
N_list = list(range(1, N+1))

for _ in range(M):
    i, j = map(int, input().split())
    N_list[i-1 : j] = reversed(N_list[i-1 : j]) #i부터 j까지(포함) 구간을 똑 떼서 뒤집은 뒤, 그 자리에 다시 꽂아 넣기

print(*N_list)


#평균
N = int(input())
M = list(map(int, input().split()))

M_max = max(M)
M_sum = sum(M)

print(M_sum * 100 / M_max / int(N)) #굳이 int 변환 안해도 됨