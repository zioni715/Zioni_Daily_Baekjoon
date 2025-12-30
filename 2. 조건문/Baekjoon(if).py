print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")


print("|\\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print("||_/=\\\\__|")

A, B = map(int, input().split())
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")


a = int(input())  #case로 써도 된다. #백준은 무조건 input()

if a >= 90:
    print("A")
elif a >= 80:
    print("B")
elif a >= 70:
    print("C")
elif a >=60:
    print("D")
else:
    print("F")


#윤년
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(1)
else:
    print(0)


#사분면
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)


#알람시계
H, M = map(int, input().split())
if M >= 45:
    M = M - 45
else:
    H = H - 1
    M = M + 15

if H < 0:
    H = 23

print(H, M)

#오븐시계
#A, B = map(int, input().split())
#C = int(input())

#if B + C >= 60:
#   A = A + 1
#    B = B + C - 60
#else:
#    A = A
#    B = B + C

#if A < 0:
#    A = 23

#print(A, B)

#오븐시계
A, B = map(int, input().split())
C = int(input())

A += C // 60
B += C % 60

if B >= 60:
    A += 1
    B -= 60
if A >= 24:
    A -= 24

print(A, B)


#주사위
a ,b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a == b or a == c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    print(max(a, b, c) * 100)

