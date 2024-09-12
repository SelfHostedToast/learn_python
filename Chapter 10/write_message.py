from pathlib import Path

num = int()
file_name = f"test{num}"

if file_name:
    num +=1

path = Path(f'Chapter 10/{file_name}.txt')
path.write_text("I love programming.")