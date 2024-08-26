prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program: "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    elif message == 'Easter Egg':
        import this
    else:
        print(message)