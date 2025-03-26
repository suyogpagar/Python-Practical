
names = input("Enter the names of students, separated by commas: ").split(',')
names_upper = [name.strip().upper() for name in names]
letter = input("Enter the letter to count occurrences of: ").upper()
lcount = sum(name.count(letter) for name in names_upper)
nldict = {name: len(name) for name in names_upper}
print("Names in uppercase:",names_upper)
print(f"Occurrences of the letter '{letter}': {lcount}")
print("Name-Length Dictionary:",nldict)
