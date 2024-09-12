# 10-1 Learning Python
from pathlib import Path

path = Path('Chapter 10/learning_python.txt')
contents = path.read_text()

print(contents)

lines = contents.splitlines()
summary = ''
for line in lines:
    summary += line

# print(summary)