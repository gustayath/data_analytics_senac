sets = {1, 2, 3, 4}
print(sets)

sets.add(5)
sets.update([6, 7, 8])

sets.add(3)

print(sets)

sets.remove(2)
sets.discard(99)
pop = sets.pop()

print(pop)
print(sets)