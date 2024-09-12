# 10-2 Learning C
from pathlib import Path

path = Path('Chapter 10/learning_python.txt')
contents = path.read_text()

print(contents.replace("Python", "C"))

lines = contents.splitlines()
summary = ''
for line in lines:
    summary += line

# print(summary)