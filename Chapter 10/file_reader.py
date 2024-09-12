from pathlib import Path

path = Path('Chapter 10/pi_digits.txt')
contents = path.read_text()

print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)