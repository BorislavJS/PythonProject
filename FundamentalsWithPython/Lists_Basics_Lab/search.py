n = int(input())
word = input()

all_string = []
string_contains_word = []

for _ in range(n):
    string = input()
    all_string.append(string)

    if word in string:
        string_contains_word.append(string)

print(all_string)
print(string_contains_word)