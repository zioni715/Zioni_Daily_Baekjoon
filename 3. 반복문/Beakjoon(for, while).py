#구구단
N = int(input())

for x in range(1, 10):
    print(f"{N} * {x} = {N * x}")


#A + B -3
#T = int(input())
#A = int(input())
#B = int(input())

#for A in range(1, 10):
#    for B in range(1, 10):
#        print(A + B)

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(A + B)

#합
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

#영수증
X = int(input())
N = int(input())
sum = 0

for i in range(N):
    a, b = map(int, input().split())
    sum += (a * b)

if X == sum:
    print("Yes")
else:
    print("No")


#코딩은 체육과목 입니다
N = int(input())

for i in range(N//4):
    print("long" + "")
print("int")

#빠른 A+B
import sys

T = int(input())
for _ in range (T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)

#A+B-7
T = int(input())

for x in range(1, T+1):
    A, B = map(int, input().split())
    print("Case #" + str(x) + ":", (A + B))


#A+B-8
T = int(input())

for x in range(1, T+1):
    A, B = map(int, input().split())
    #print("Case #" + str(x) + ":", str(A)+ "+" + str(B), "=", (A + B))
    print(f"Case #{x}: {A} + {B} = {A + B}")

#별찍기-1

N = int(input())
for i in range(1, N+1):
    print("*"* i)

#별찍기-2

N = int(input())
for i in range(1, N+1):
#    print(str("")*(N-i), "*"* i)
    print(" "*(N-i) + "*"* i)

#A + B -5
while True:
    try:
        A, B = map(int, input().split())
        if A == 0 and B == 0:
                break

        else:
            print(A + B)
    except:
        break

# A + B - 4
while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except EOFError:
        break

