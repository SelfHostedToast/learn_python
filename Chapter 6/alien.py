alien_0 = {'color': 'green', 'points': 5}

print(alien_0)
print(alien_0['color'])
print(alien_0['points'])

# Print the value for the 'points' key
new_points = alien_0['points']

print(f"You just earned {new_points} points!")

# Dictionaries are dynamic structures, you can add key-value pairs at any time.

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Changing the value of alien 0's color key
alien_0['color'] = 'yellow'

print(f"The alien is {alien_0['color']}")

alien_0['speed'] = 'medium'

print(f"Original Position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment.

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

del alien_0['points']
print(alien_0)

