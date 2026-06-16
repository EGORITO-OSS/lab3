with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
    lines = len(text)
    f.close()

with open('input.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
total = 0
for row in data:
    total += len(row.split())
    f.close()

with open('statistics.txt', 'w', encoding='utf-8') as f:
    f.write("Количество строк: " + str(lines) + "\n")
    f.write("Общее количество слов: " + str(total))
    f.close()