# 문제 : 그룹 단어 체커

'''
문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고,
kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다.
N은 100보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에 단어가 들어온다.
단어는 알파벳 소문자로만 이루어져 있으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.
'''


def group_word_checker(word):
  seen = set() # set함수는 중복을 자동으로 제거
  for i in range(len(word)):
    if word[i] in seen:
      if i > 0 and word[i] != word[i-1]: # 그룹 단어 체커의 핵심 조건은 바로 직전 글자와 비교해야함
        return False # 직전 글자와 다르면 그룹 단어가 아니니까 False 반환
    else:
      seen.add(word[i])
  return True

N = int(input())
count = 0

for _ in range(N):
  word = input().strip()
  if group_word_checker(word):
    count += 1

print(count)