data = []

with open("words.txt", "r", encoding="utf-8") as f:
    for line in f:
        data.append(line.strip())

alpha = sorted(data)
by_len = sorted(data, key=len)
reversed_words = sorted(data, reverse=True)

with open("sorted_alphabetically.txt", "w", encoding="utf-8") as f:
    for item in alpha:
        f.write(item + "\n")

with open("sorted_by_length.txt", "w", encoding="utf-8") as f:
    for item in by_len:
        f.write(item + "\n")

with open("sorted_reverse.txt", "w", encoding="utf-8") as f:
    for item in reversed_words:
        f.write(item + "\n")

print("Файлы созданы")