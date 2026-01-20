import sys
import pyperclip


def find_narrow_spaces(filename):
    narrow_space = '\u202F'   # узкий пробел
    em_dash = '\u2014'        # —
    nbsp = '\u00A0'           # неразрывный пробел
    arrow = '\u2192'          # →

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    count = [0, 0, 0, 0]

    found = False
    for i, line in enumerate(lines, start=1):
        if narrow_space in line:
            print(f"Строка {i}: {line.strip()}")
            print("→ Найден узкий пробел (U+202F) на позиции: ", end='')
            positions = [str(pos) for pos, char in enumerate(line) if char == narrow_space]
            print(", ".join(positions))
            found = True
            count[0] += len(positions)

        if em_dash in line:
            print(f"Строка {i}: {line.strip()}")
            print("→ Найдено длинное тире (U+2014) на позиции: ", end='')
            positions = [str(pos) for pos, char in enumerate(line) if char == em_dash]
            print(", ".join(positions))
            found = True
            count[1] += len(positions)

        if nbsp in line:
            print(f"Строка {i}: {line.strip()}")
            print("→ Найден неразрывный пробел (U+00A0) на позиции: ", end='')
            positions = [str(pos) for pos, char in enumerate(line) if char == nbsp]
            print(", ".join(positions))
            found = True
            count[2] += len(positions)

        if arrow in line:
            print(f"Строка {i}: {line.strip()}")
            print("→ Найдена стрелка (U+2192) на позиции: ", end='')
            positions = [str(pos) for pos, char in enumerate(line) if char == arrow]
            print(", ".join(positions))
            found = True
            count[3] += len(positions)

    if not found:
        print("Специальные символы в файле не найдены.")
    else:
        print(
            "Найдено:\n"
            f"\tузкий пробел: {count[0]}\n"
            f"\tдлинное тире: {count[1]}\n"
            f"\tнеразрывный пробел: {count[2]}\n"
            f"\tстрелка →: {count[3]}"
        )



if __name__ == "__main__":
    if len(sys.argv) > 1:
        find_narrow_spaces(sys.argv[1])
    else:
        clipboard_text = pyperclip.paste()
        with open("sample.txt", "w", encoding="utf-8") as f:
            f.write(clipboard_text)
        find_narrow_spaces("sample.txt")
