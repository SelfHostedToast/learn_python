# 10-1 Learning Python
from pathlib import Path

path = Path('Chapter 10/learning_python.txt')
contents = path.read_text()

print(contents)

summary = ''
for line in contents.splitlines():
    summary += line

# print(summary)