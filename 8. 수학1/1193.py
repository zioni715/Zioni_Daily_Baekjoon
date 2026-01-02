# 문제 : 분수찾기

'''
문제
무한히 큰 배열에 다음과 같이 분수들이 적혀있다.
이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

출력
첫째 줄에 분수를 출력한다.
'''
'''
X = 1 : 1/1
X = 2 : 1/2 , X = 3 : 2/1
X = 4 : 3/1 , X = 5 : 2/2 , X = 6 : 1/3
X = 7 : 1/4 , X = 8 : 2/3 , X = 9 : 3/2 , X = 10 : 4/1
X = 11 : 5/1 , X = 12 : 4/2 , X = 13 : 3/3 , X = 14 : 2/4 , X = 15 : 1/5
규칙을 찾아보면
for i in range(X):
    n+=1
    그리고 분자 + 분모 = n+1
    그리고 n에 따라 분자가 +1씩 분모가 -1씩
                    분자가 -1씩 분모가 +1씩
'''
# n번째 대각선까지의 누적 개수는 삼각수
# T_n = 1 + 2 + ... + n = n(n+1)/2
# T_n >= X를 만족하는 n이 X가 속한 대각선 번호

def find_fraction(X):
    n = 1
    remain = 0
    while remain + n < X:
        remain += n
        n += 1

    idx = X - remain
    if n % 2 == 0:
        numerator = idx
        denominator = n - idx + 1
    else:
        numerator = n - idx + 1
        denominator = idx
    return f"{numerator}/{denominator}"

X = int(input())
print(find_fraction(X))
