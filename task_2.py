word = input("Введите слово для поиска: ").strip()
word_low = word.lower()

found_lines = []
all_count = 0

with open('text.txt', 'r', encoding='utf-8') as f:
    for num, line in enumerate(f, start=1):
        line_low = line.lower()
        count_line = line_low.count(word_low)

        if count_line > 0:
            all_count += count_line
            found_lines.append(num)

if all_count > 0:
    answer = "Да"
else:
    answer = "Нет"

print(f"Слово найдено: {answer}")
print(f"Сколько раз оно встречается: {all_count}")
print(f"В каких строках встречается: {found_lines}")

with open("search_results.txt", "w", encoding="utf-8") as out:
    out.write(f"Введённое слово: {word}")
    out.write(f"\nСлово найдено: {answer}")
    out.write(f"\nСколько раз оно встречается: {all_count}")
    out.write(f"\nВ каких строках встречается: {found_lines}")