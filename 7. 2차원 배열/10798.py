# 문제 : 세로읽기

'''
문제 
아직 글을 모르는 영석이가 벽에 걸린 칠판에 자석이 붙어있는 글자들을 붙이는 장난감을 가지고 놀고 있다.
이 장난감에 있는 글자들은 영어 대문자 'A'부터 'Z', 영어 소문자 'a'부터 'z', 숫자 '0'부터 '9'이다.
영석이는 칠판에 글자들을 수평으로 일렬로 붙여서 단어를 만든다.
다시 그 아래쪽에 글자들을 붙여서 또 다른 단어를 만든다.
이런 식으로 다섯 개의 단어를 만든다. 

입력
총 다섯줄의 입력이 주어진다.
각 줄에는 최소 1개, 최대 15개의 글자들이 빈칸 없이 연속으로 주어진다.
주어지는 글자는 영어 대문자 'A'부터 'Z', 영어 소문자 'a'부터 'z', 숫자 '0'부터 '9' 중 하나이다. 
각 줄의 시작과 마지막에 빈칸은 없다.

출력
영석이가 세로로 읽은 순서대로 글자들을 출력한다.
이때, 글자들을 공백 없이 연속해서 출력한다.
'''

def read_vertically(words):
  result = []
  max_length = max(len(word) for word in words) # 5개 단어 중 가장 긴 단어의 길이
  for i in range(max_length): # 세로로 읽기 시작하는 부분
    for word in words:
      if i < len(word):
        result.append(word[i])
  return ''.join(result) # 리스트에 모인 글자들을 공백 없이 이어붙여 하나의 문자열로 반환

words = [input().strip() for _ in range(5)]
output = read_vertically(words)
print(output)