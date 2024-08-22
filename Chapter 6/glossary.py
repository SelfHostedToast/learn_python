glossary = {'variable': 'a placeholder for data in programming', 'conditional statement': 'a statement that evaluates either true or false', 'integer': 'a number in programming', 'for loop': 'a kind of programming loop that runs based on a provided range', 'dictionary': 'an abstraction used in programming to group like items in a "key-value" pair relationship', 'method': 'a built-im way of modifying a statement in programming', 'interpreter': 'the "middle-man" of sorts that converts code into machine code for computers to understand', 'list': 'a list is a programming data structure that allows similar data to be stored', 'program': 'a set of instructions for a computer or machine to follow explicitly, developed by a programmer', 'web application': 'a program written in a way that allows it to be interfaced via a web browser'}

print("Glossary of Programming Terminology:\n")

for word, definition in glossary.items():
    print(f"A(n) {word} is defined as: {definition}.\n")