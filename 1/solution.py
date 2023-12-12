file = open("input.txt", "r")

def find_first_number(line):
    for character in line:
        if character.isnumeric():
            return character

def find_last_number(line):
    for character in line[::-1]:
        if character.isnumeric():
            return character

def find_first_and_last_numbers(file):
    list_of_numbers = []
    for line in file.readlines():
        list_of_numbers.append(f"{find_first_number(line)}{find_last_number(line)}")

    total = 0
    for number in list_of_numbers:
        total = total + int(number)
        print(total)

find_first_and_last_numbers(file)
