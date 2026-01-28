# 문제 : 좌표 정렬하기 2

'''
문제
2차원 평면 위의 점 N개가 주어진다.
좌표를 y가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력 
첫째 줄에 점의 개수 N이 주어진다.
둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다.
좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

출력
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
'''

N = int(input())
locations = []

for _ in range(N):
  x, y = list(map(int, input().split()))
  locations.append([x, y])

locations.sort(key=lambda n : (n[1], n[0])) # y에 대한 오름차순 -> x에 대한 기준도 줘야함

for x, y in locations:
  print(x, y)