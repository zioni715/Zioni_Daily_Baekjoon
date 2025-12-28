# 단어 공부

'''
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''

# 1. 문자열을 받는데 대소문자 구분 없이 받아야하고, 대문자로 출력해야 하니까 일단 다 대문자로 바꾸기!
# 그리고 리스트로 변환해줘야 할 듯...?
word = input().upper()
word_list = list(set(word))
most_word = []

# 2. 알파벳 개수 세려면 어떻게 할까
for char in word_list:
  count = word_list.count(char)
  most_word.append(count)

if most_word.count(max(most_word)) > 1:
  print("?")
else:
  max_index = most_word.index(max(most_word))
  print(word_list[max_index])

# 왜 시간초과가 뜨지....?
# 아 이거 어렵다 진짜!!!!

from collections import Counter

def find_most_frequency_char(word):
  word = word.upper()
  char_count = Counter(word)
  max_freq = max(char_count.values())

  most_frequency_char = char_count.most_common()
  result = [char for char, count in most_frequency_char if count == max_freq]

  if len(result) > 1:
    return "?"
  else:
    return result[0]

word = input()
print(find_most_frequency_char(word))