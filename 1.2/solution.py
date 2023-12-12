import re
import time

print('RUNNING')

numbers_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def check_string(sub_string):
    for key in numbers_dict:
        if key in sub_string:
            return numbers_dict[key]
    return None

def find_first_number(line):
    for i, character in enumerate(line):
        if character.isnumeric():
            return character
        elif i < len(line) - 1 and line[i + 1].isnumeric():
            return line[i + 1]
        else:
            found = check_string(line[i:i + 5])
            if found:
                return found

def find_last_number(line):
    for i in range(len(line) - 1, -1, -1):
        if line[i].isnumeric():
            return line[i]
        elif i > 0 and line[i - 1].isnumeric():
            return line[i - 1]
        else:
            found = check_string(line[max(i - 4, 0):i + 1])
            if found:
                return found

def find_first_and_last_numbers(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        
    numbers = [f"{find_first_number(line.rstrip())}{find_last_number(line.rstrip())}" for line in lines]
    total = sum(int(number) for number in numbers if number.isdigit())
    print(total)

start_time = time.time()
find_first_and_last_numbers("input.txt")
end_time = time.time()
duration = end_time - start_time
print("Duration in seconds:", duration)