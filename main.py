# Является ли строка палиндромом?


def main():
    line = input("Enter line: ")
    left, right = 0, len(line) - 1

    while left < right:
        while left < right and not line[left].isalnum():
            left += 1
        while left < right and not line[right].isalnum():
            right -= 1

        if line[left].lower() != line[right].lower():
            return False

        left += 1
        right -= 1

    return True


print(main())
