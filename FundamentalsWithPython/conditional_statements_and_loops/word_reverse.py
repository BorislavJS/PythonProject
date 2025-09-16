# word = input()
#
# print(word[::-1])

# word = input()
#
# for i in word[::-1]:
#     print(i, end= "")

word = input()

reverse_word = ""

for i in range(len(word)-1, -1, -1):
    reverse_word += word[i]
print(reverse_word)


