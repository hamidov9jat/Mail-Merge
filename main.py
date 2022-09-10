# Get all names from the list of names file
with open('Input/Names/invited_names.txt') as f:
    all_names = list(map(str.strip, f.readlines()))

print(all_names)

# Make a letter template
with open('Input/Letters/starting_letter.txt') as f:
    letter_template = f.read()

# Create letter to each person in the list based on template
for name in all_names:
    with open(f'Output/ReadyToSend/letter_for_{name}.txt', mode='w') as f:
        letter = letter_template.replace('[name]', name)
        f.write(letter)
