# 문제 : 약수들의 합
'''
문제 
어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다.
예를 들어, 6은 = 1 + 2 + 3 으로 완전수이다.
n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.

입력
입력은 테스트 케이스마다 한 줄 간격으로 n이 주어진다.
입력의 마지막엔 -1 이 주어진다.

출력
테스트 케이스마다 한줄에 하나씩 출력해야 한다.
n이 완전수라면, n을 n이 아닌 약수들의 합으로 나타내어 출력한다.
이때, 약수들은 오름차순으로 나열해야 한다.
n이 완전수가 아니라면 n is NOT perfect. 를 출력한다.
'''

# 1번 오답
def check_perfect(n):
  measure = []
  cnt = 0
  for i in range(1, n+1):
    if n % i == 0:
      measure.append[i]
      cnt += 1
      if cnt == n:
        break

  if sum(measure) == n:
    for i, num in enumerate(measure):
      total_sum += num
      calculation_string += str(num)
      if i < len(measure) - 1:
        calculation_string += " + "
        print(f"{total_sum} = {calculation_string}")
  
  else:
    print(f"{n} is NOT perfect.")

  return

result = []

while True:
  n = int(input())

  if n == -1:
    break

  result.append(check_perfect(n))

print("\n".join(result))


# ===================

def check_perfect(n):
  measure = []
  for i in range(1, n):
    if n % i == 0:
      measure.append(i)

  if sum(measure) == n:
    return f"{n} = " + " + ".join(map(str, measure))
  else:
    return f"{n} is NOT perfect."

result = []

while True:
  n = int(input())

  if n == -1:
    break

  result.append(check_perfect(n))

print("\n".join(result))