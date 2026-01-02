import sys
import pyperclip


def find_narrow_spaces(filename):
    narrow_space = '\u202F'
    em_dash = '\u2014'
    nbsp = '\u00A0'

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    count = [0,0,0]

    found = False
    for i, line in enumerate(lines, start=1):
        if narrow_space in line:
            print(f"Строка {i}: {line.strip()}")
            print(f"→ Найден узкий пробел (U+202F) на позиции: ", end='')
            positions = [str(pos) for pos, char in enumerate(line) if char == narrow_space]
            print(", ".join(positions))
            found = True
            count[0] += 1
        if em_dash in line:
            print(f"Строка {i}: {line.strip()}")
            print(f"→ Найден длинное тире (U+2014) на позиции: ", end='')
            positions = [str(pos) for pos, char in enumerate(line) if char == em_dash]
            print(", ".join(positions))
            found = True
            count[1] += 1
        if nbsp in line:
            print(f"Строка {i}: {line.strip()}")
            print(f"→ Найден неразрывный пробел (U+AO) на позиции: ", end='')
            positions = [str(pos) for pos, char in enumerate(line) if char == em_dash]
            print(", ".join(positions))
            found = True
            count[2] += 1

    if not found:
        print("Узкий пробел или длинное тире или неразрывный пробел в файле не найдены.")
    else:
        print(f'Найдено:\n\tузкий пробел: {count[0]}\n\tдлинное тире: {count[1]}\n\tнеразрывный пробел: {count[2]}')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        find_narrow_spaces(sys.argv[1])
    else:
        clipboard_text = pyperclip.paste()
        with open("sample.txt", "w", encoding="utf-8") as f:
            f.write(clipboard_text)
        find_narrow_spaces("sample.txt")
