# 8-10 Sending Messages
def show_message(new_message_list, sent_message_list):
    # Uncomment the two lines below to see list transfer.
    # print(new_message_list)
    # print(sent_message_list)
    while new_message_list:
        message_comp = new_message_list.pop()
        sent_message_list.append(message_comp)

new_message_list = ['Good Morning!', 'You still coming to dinner tonight?', 'I had a blast, see you soon!']
sent_message_list = []
show_message(new_message_list,sent_message_list)

print(new_message_list)
print(sent_message_list)