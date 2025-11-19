# 숫자의 합
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 숫자의 개수 N(1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백 없이 주어진다.
# 출력 : 입력으로 주어진 숫자 N개의 합을 출력한다.

# N = int(input())

# numbers = []

# for i in range(N):
#   numbers.append(int(input())) # append()는 리스트의 맨 뒤에 새로운 요소를 추가하는 함수  

# sum_numbers = sum(numbers)
# print(sum_numbers)

#=================================

# M = int(input())

# numbers = list(map(int, input())) # map()은 리스트의 모든 원소에 대해 특정한 함수를 적용할 때 사용하는 함수 

# sum_numbers = sum(numbers)
# print(sum_numbers)

#  =================================

N = input() # 숫자의 개수는 필요 없으므로 변수에 저장하지 않음
numbers = input() # 숫자들을 문자열로 입력 받음
total = 0 # 합계를 저장할 변수 초기화

for i in numbers: # 문자열의 각 문자에 대해 반복
  total += int(i) # 문자를 정수로 변환하여 합계에 더함

print(total)
