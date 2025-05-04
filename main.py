import sys


def find_narrow_spaces(filename):
    narrow_space = '\u202F'
    em_dash = '\u2014'
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

    if not found:
        print("Узкий пробел или длинное тире в файле не найдены.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        find_narrow_spaces(sys.argv[1])
    else:
        find_narrow_spaces("sample.txt")
