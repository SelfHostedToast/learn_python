# squares = []
# for value in range (1,101):
#   square = value ** 2
#   squares.append(square)
# print(squares)

# We can make this code more consise by ommiting the sqaure = value ** 2 line

squares = []
for value in range (1,51):
  squares.append(value**2)
print(squares)

# We can find statistics of our numbers using the min, max, and sum functions
print(min(squares))
print(max(squares))
print(sum(squares))
