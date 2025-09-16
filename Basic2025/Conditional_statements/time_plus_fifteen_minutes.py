hours = int(input())
minutes = int(input())

# Добавяме 15 минути
minutes += 15

# Ако минутите станат 60 или повече, коригираме часа и минутите
if minutes >= 60:
    hours += 1
    minutes -= 60

# Ако часовете станат 24, връщаме ги на 0
if hours == 24:
    hours = 0

# Отпечатваме резултата във форматиран вид
print(f"{hours}:{minutes:02d}")
