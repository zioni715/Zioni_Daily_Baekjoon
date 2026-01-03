# 문제 : 소수 찾기
'''
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. 
N은 100이하이다.
다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.
'''

# 1번 오답
def find_prime(n):
  cnt = 0
  if n <= 1:
    cnt += 0
  for i in range(2, n):
    if n % i == 0:
      cnt += 0
    else:
      cnt += 1
  return f"{cnt}"

N = int(input())
cnt = 0
for i in range(N):
  nums = list(map(int, input().split()))
for num in nums:
  find_prime(num)

# ========================


def find_prime(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

N = int(input())
nums = []
while len(nums) < N:
  nums += list(map(int, input().split()))

cnt = 0
for num in nums:
  if find_prime(num):
    cnt += 1

print(cnt)