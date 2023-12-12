print('RUNNING')
file = open("input.txt", "r")

def find_first_number(line):
    for i in range(len(line)):
        if line[i].isnumeric():
            return line[i]
        else:
            if 'one' in line[i:i+5]:
                return 1
            if 'two' in line[i:i+5]:
                return 2
            if 'three' in line[i:i+5]:
                return 3
            if 'four' in line[i:i+5]:
                return 4
            if 'five' in line[i:i+5]:
                return 5
            if 'six' in line[i:i+5]:
                return 6
            if 'seven' in line[i:i+5]:
                return 7
            if 'eight' in line[i:i+5]:
                return 8
            if 'nine' in line[i:i+5]:
                return 9
                        
            

def find_last_number(line):
    for i in range(len(line)):
        i = i + 1
        if line[len(line)-i].isnumeric():
            return line[len(line)-i]
        else:
            point_1 = len(line)-i+1
            point_2 = len(line)-i-5
            if 'one' in line[point_2:point_1]:
                return 1
            if 'two' in line[point_2:point_1]:
                return 2
            if 'three' in line[point_2:point_1]:
                return 3
            if 'four' in line[point_2:point_1]:
                return 4
            if 'five' in line[point_2:point_1]:
                return 5
            if 'six' in line[point_2:point_1]:
                return 6
            if 'seven' in line[point_2:point_1]:
                return 7
            if 'eight' in line[point_2:point_1]:
                return 8
            if 'nine' in line[point_2:point_1]:
                return 9

def find_first_and_last_numbers(file):
    list_of_numbers = []
    for line in file.readlines():
        print(line)
        print(f"{find_first_number(line)}{find_last_number(line)}")
        list_of_numbers.append(f"{find_first_number(line)}{find_last_number(line)}")

    total = 0
    for number in list_of_numbers:
        total = total + int(number)
    print(total)

find_first_and_last_numbers(file)
