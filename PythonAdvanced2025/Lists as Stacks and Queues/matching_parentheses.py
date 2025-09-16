# text = input()
# parentheses = []
#
# for i in range(len(text)):
#     if text[i] == "(":
#         parentheses.append(i)
#     elif text[i] == ")":
#         start_index = parentheses.pop()
#         print(text[start_index:i + 1])



# expression = input()
#
# stack = []
#
# for index in range(len(expression)):
#     if expression[index] == "(":
#         stack.append(index)
#     elif expression[index] == ")":
#         start_index = stack.pop()
#         end_index = index + 1
#         print(expression[start_index:end_index])

# expression = input()
#
# # Тук създавам празен списък, които ще използвам като стек за отварящите скоби
# stack = []
#
# # Обхождам всеки символ по индек
# for index in range(len(expression)):
#     if expression[index] == "(":  # Ако намеря отваряща скоба, запомняме къде е индекса й
#         stack.append(index)
#     elif expression[index] == ")":
#         # Вземаме последния индекс на отваряща скоба (
#         start_index = stack.pop()
#         # Крайният индекс е този на ) + 1, за да включим и нея
#         end_index = index + 1
#         #Печатаме израза в скоби
#         print(expression[start_index:end_index])


expression = input()
stack = []

for index in range(len(expression)):
    if expression[index] == "(":
        stack.append(index)
    elif expression[index] == ")":
        start_index = stack.pop()
        end_index = index + 1
        print(expression[start_index:end_index])




