# 다이얼

# 상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.
# 전화를 걸고 싶은 번호가 있다면, 숫자 하나를 누른 다음에 금속 핀이 있는 곳까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
# 숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해서는 1초씩 더 걸린다.
# 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 
# 예를 들어, UNUCIC는 868242와 같다. 할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2 보다 크거나 같고, 15보다 작거나 같다.
# 출력 : 첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.

# S = input()
# time = 0

# for char in S:
#   if char in 'ABC':
#     time +=3
#   elif char in 'DEF':
#     time +=4
#   elif char in 'GHI':
#     time +=5
#   elif char in 'JKL':
#     time +=6
#   elif char in 'MN0':
#     time +=7
#   elif char in 'PQRS':
#     time +=8
#   elif char in 'TUV':
#     time +=9
#   elif char in 'WXYZ':
#     time +=10

# print(time)


S = input()
arr = [ 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

for char in S:
  for i in range(len(arr)):
    if char in arr[i]:
      time += i + 3

print(time)


"""
arr = [ 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'] 는 문자열들의 리스트
arr[0] 은 'ABC'
arr[1] 은 'DEF'
을 의미한다. 

time = 0 으로 시간 초기화

for char in S: 는 S에 들어있는 문자열을 한 글자씩 꺼내서 반복
  for i in range(len(arr)): 는 arr 리스트의 인덱스를 0부터 7까지 반복
    if char in arr[i]: 는 char가 arr 리스트의 i번째 문자열에 포함되어 있는지 확인
      time += i + 3 는 해당 문자가 속한 그룹의 인덱스 i에 3을 더한 값을 time에 누적하는 역할을 한다.






"""
