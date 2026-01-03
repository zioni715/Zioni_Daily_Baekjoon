# 문제 : 직사각형
'''
문제 
정수 A, B가 주어진다.
세로 길이가 Acm, 가로 길이가 Bcm인 아래와 같은 직사각형의 넓이 cm^2 단위로 구하시오.

입력
표준 입력에 다음과 같은 형태로 입력이 주어진다.

출력
세로 길이가 Acm, 가로 길이가 Bcm인 직사각형의 넓이를 cm^2단위로 구하고, 단위(cm^2)를 생략하여 출력한다.
'''

def area_rectangle(A, B):
  area = A * B
  return area

A = int(input())
B = int(input())
print(area_rectangle(A, B))