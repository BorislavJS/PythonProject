sequence = input()

stack = []

pairs = {')': '(', '}': '{', ']': '['}

for symbol in sequence:
    if symbol in "({[":
        stack.append(symbol)
    elif symbol in ")}]":
        if not stack or stack[-1] != pairs[symbol]:
            print("NO")
            break
        else:
            stack.pop()
else:
    if not stack:
        print("YES")
    else:
        print("NO")
