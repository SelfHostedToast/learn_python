# 7-2 Restaurant Seating

party_size = input("Please enter the size of your party so that we can seat you accordingly: ")

party_size = int(party_size)

if party_size > 8:
    print(f"Unfortunately with your party size of {party_size}, there is a bit of a wait before you'll be seated.")
else:
    print(f"Your party of {party_size} is ready to be seated, please follow me!")