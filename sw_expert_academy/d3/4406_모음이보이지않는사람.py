import sys
sys.stdin = open("4406_input.txt")
vowels = "aeiou"
for tc in range(int(input())):
    result = ""
    strings = input()
    for char in strings:
        if not char in vowels:
            result += char

    print(f"#{tc + 1} {result}")