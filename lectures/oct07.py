"""Practice with for loops + range()"""

pets: list[str] = ["Louie", "Bo", "Bear"]
"""Tell every pet they are a good boy"""
for animal in pets:
    print(f"Good boy, {animal}!")

for index in range(0, len(pets)):
    print(pets[index])

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")
