# 문제 : 좌표 압축

'''
문제
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다.
이 좌표에 좌표 압축을 적용하려고 한다.
Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.
X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

입력
첫째 줄에 N이 주어진다.
둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

출력
첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.
'''
N = int(input())

location_x = list(map(int, input().split()))

arranged_x = sorted(list(set(location_x)))

zip_dict = {}
i = 0
for val in arranged_x:
  zip_dict[val] = i
  i += 1

result = []
for x in location_x:
  result.append(zip_dict[x])

print(" ".join(map(str, result)))

# ======================

# for i in range(0, N):
#   for j in range(i+1, N):
#     zip_x = location_x[i] - location_x[j]
#     if zip_x > 0:
#       zip_list[i] += 1
#     else:
#       zip_list[i] += 0

# print(" ".join(map(str, zip_list)))