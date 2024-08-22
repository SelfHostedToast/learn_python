wood_types = ['oak', 'spruce', 'acacia', 'birch', 'cherry', 'dark oak']
stone_types = ['stone', 'cobblestone', 'deepslate', 'cobbled deepslate', 'andesite', 'diorite', 'granite']

wood_types.sort()
stone_types.sort()

print("The following are the wood types you can obtain in Minecraft:")
for logs in wood_types:
  print(f"{logs}\n")
print("Next we will list the types of stone you'll find caving in Minecraft:")
for stone in stone_types:
  print(f"{stone}\n")