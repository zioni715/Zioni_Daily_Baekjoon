# 문제 : 수 정렬하기 3

'''
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N이 주어진다.
둘째 줄부터 N개의 줄에는 수가 주어진다. 
이 수는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''

# import sys

# N = int(sys.stdin.readline())
# nums = [int(sys.stdin.readline()) for _ in range(N)]

# arranged_nums = sorted(nums)
# for num in arranged_nums:
#   print(num)

# 메모리 초과

# ==========

# N = int(input())
# nums = []

# for i in range(N):
#   i = int(input())
#   nums.append(i)

# arranged_nums = sorted(nums)
# for num in arranged_nums:
#   print(num)

# 메모리 초과
# ========== 


# N = int(input())
# nums = []

# for i in range(N):
#   i = int(input())
#   nums.append(i)

# nums.sort()

# for num in nums:
#   print(num)



# import sys

# N = int(sys.stdin.readline())
# nums = [int(sys.stdin.readline()) for _ in range(N)]

# nums.sort()

# for num in nums:
#   print(num)



import sys
from array import array

input = sys.stdin.buffer.readline
write = sys.stdout.write

N = int(input())

cnt = array('I', [0]) * 10001

for _ in range(N):
    cnt[int(input())] += 1

CHUNK = 10000
for i in range(1, 10001):
    c = cnt[i]
    if c:
        line = f"{i}\n"
        while c > 0:
            k = CHUNK if c > CHUNK else c
            write(line * k)
            c -= k

