'''
You are given n words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
See the sample input/output for clarification.
Note: Each input line ends with a "\n" character.
'''
n = int(input())
dic  = {}

for _ in range(n):
  w = input()
  if w in dic.keys():
    dic[w]+=1
  else:
    dic.update({w:1})

print(len(dic.keys()))
print(*dic.values())