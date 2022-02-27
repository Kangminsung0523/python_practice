numbers = [1, 2, 3]
magic_numbers = list(map(lambda x: 3*x+6, numbers))
print(magic_numbers)

def magic_wand(x):
    return 3*x+6

magic_numbers = list(map(magic_wand, numbers))