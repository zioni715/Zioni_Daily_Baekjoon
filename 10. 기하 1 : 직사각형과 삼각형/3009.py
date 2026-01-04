# 문제 : 네 번째 점
'''
문제
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

입력
세 점의 좌표가 한 줄에 하나씩 주어진다. 
좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

출력
직사각형의 네 번째 점의 좌표를 출력한다.
'''

dots = []

for i in range(3):
  x, y = list(map(int, input().split()))
  dots.append([x, y])

x_values = [dot[0] for dot in dots]
y_values = [dot[1] for dot in dots]

unique_x = 0
for x in x_values:
  if x_values.count(x) == 1:
    unique_x = x
    break

unique_y = 0
for y in y_values:
  if y_values.count(y) == 1:
    unique_y = y
    break

print(unique_x, unique_y)