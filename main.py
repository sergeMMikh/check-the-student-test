import sys
import pyperclip


def find_narrow_spaces(filename):
    narrow_space = '\u202F'
    em_dash = '\u2014'
    nbsp = '\u00A0'

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    found = False
    for i, line in enumerate(lines, start=1):
        if narrow_space in line:
            print(f"Строка {i}: {line.strip()}")
            print(f"→ Найден узкий пробел (U+202F) на позиции: ", end='')
            positions = [str(pos) for pos, char in enumerate(line) if char == narrow_space]
            print(", ".join(positions))
            found = True
        if em_dash in line:
            print(f"Строка {i}: {line.strip()}")
            print(f"→ Найден длинное тире (U+2014) на позиции: ", end='')
            positions = [str(pos) for pos, char in enumerate(line) if char == em_dash]
            print(", ".join(positions))
            found = True
        if nbsp in line:
            print(f"Строка {i}: {line.strip()}")
            print(f"→ Найден неразрывный пробел (U+AO) на позиции: ", end='')
            positions = [str(pos) for pos, char in enumerate(line) if char == em_dash]
            print(", ".join(positions))
            found = True

    if not found:
        print("Узкий пробел или длинное тире или неразрывный пробел в файле не найдены.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        find_narrow_spaces(sys.argv[1])
    else:
        clipboard_text = pyperclip.paste()
        with open("sample.txt", "w", encoding="utf-8") as f:
            f.write(clipboard_text)
        find_narrow_spaces("sample.txt")
