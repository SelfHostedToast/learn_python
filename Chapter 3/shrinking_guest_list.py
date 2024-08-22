guest_list = ['BENEE', 'Skrillex', 'RUFUS DU SOL', 'Lunchbox', 'EthosLab']

invitation = f"I am so excited to be extending this formal invite to you {guest_list[0]}, We are going to have a blast together!"
print(invitation)
invitation = f"I am so excited to be extending this formal invite to you {guest_list[1]}, We are going to have a blast together!"
print(invitation)
invitation = f"I am so excited to be extending this formal invite to you {guest_list[2]}, We are going to have a blast together!"
print(invitation)
invitation = f"I am so excited to be extending this formal invite to you {guest_list[3]}, We are going to have a blast together!"
print(invitation)
invitation = f"I am so excited to be extending this formal invite to you {guest_list[4]}, We are going to have a blast together!"
print(invitation)

print(f"It appears that unfortunately, {guest_list[-1]} will not be attending the event tonight.")

guest_list.remove('EthosLab')
guest_list.append('Lil Uzi Vert')

invitation = f"I am so excited to be extending this formal invite to you {guest_list[0]}, We are going to have a blast together!"
print(invitation)
invitation = f"I am so excited to be extending this formal invite to you {guest_list[1]}, We are going to have a blast together!"
print(invitation)
invitation = f"I am so excited to be extending this formal invite to you {guest_list[2]}, We are going to have a blast together!"
print(invitation)
invitation = f"I am so excited to be extending this formal invite to you {guest_list[3]}, We are going to have a blast together!"
print(invitation)
invitation = f"I am so excited to be extending this formal invite to you {guest_list[4]}, We are going to have a blast together!"
print(invitation)

print("We got a table size upgrade!\nLet's invite more guests shall we?")

# Insert new guest at beginning of list
guest_list.insert(0, 'Flume')

# Insert new guest at the middle of the list

guest_list.insert(3, 'Oliver Heldens')

# Insert new guest at the end of the list

guest_list.append('Tiesto')

invitation = f"I am so excited to be extending this formal invite to you {guest_list[0]}, We are going to have a blast together!"
print(invitation)

invitation = f"I am so excited to be extending this formal invite to you {guest_list[1]}, We are going to have a blast together!"
print(invitation)

invitation = f"I am so excited to be extending this formal invite to you {guest_list[2]}, We are going to have a blast together!"
print(invitation)

invitation = f"I am so excited to be extending this formal invite to you {guest_list[3]}, We are going to have a blast together!"
print(invitation)

invitation = f"I am so excited to be extending this formal invite to you {guest_list[4]}, We are going to have a blast together!"
print(invitation)

invitation = f"I am so excited to be extending this formal invite to you {guest_list[5]}, We are going to have a blast together!"
print(invitation)

invitation = f"I am so excited to be extending this formal invite to you {guest_list[6]}, We are going to have a blast together!"
print(invitation)

invitation = f"I am so excited to be extending this formal invite to you {guest_list[7]}, We are going to have a blast together!"
print(invitation)

print("Oh no! The table won't be set in time for our reservation, I will need to adjust the guest list.")

unsend = guest_list.pop(-1)

print(f"Unfortunately {unsend}, Our reservation will not be ready in time for us. I apologize for the inconvience this may have caused.")

unsend = guest_list.pop(-1)

print(f"Unfortunately {unsend}, Our reservation will not be ready in time for us. I apologize for the inconvience this may have caused.")

unsend = guest_list.pop(-1)

print(f"Unfortunately {unsend}, Our reservation will not be ready in time for us. I apologize for the inconvience this may have caused.")

unsend = guest_list.pop(-1)

print(f"Unfortunately {unsend}, Our reservation will not be ready in time for us. I apologize for the inconvience this may have caused.")

unsend = guest_list.pop(-1)

print(f"Unfortunately {unsend}, Our reservation will not be ready in time for us. I apologize for the inconvience this may have caused.")

unsend = guest_list.pop(-1)

print(f"Unfortunately {unsend}, Our reservation will not be ready in time for us. I apologize for the inconvience this may have caused.")

print(f"Just a quick update {guest_list[0]}, Our reservation was changed and not everyone will still be attending. There is no change on your part however\nYou are still welcome to come!")

print(f"Just a quick update {guest_list[1]}, Our reservation was changed and not everyone will still be attending. There is no change on your part however\nYou are still welcome to come!")

del guest_list[-1] # removed the last two guests on the list
del guest_list[-1]

print(guest_list) # print the empty guest list