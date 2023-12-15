def check_minimum_balls(game):
    game = game.split(':')
    rounds = game[1].split(';')
    ball_counter = {
        'red' : 0,
        'green' : 0,
        'blue' : 0
    }
    for round in rounds:
        events = round.split(',')
        for event in events:
            entities = event.split()[::-1]
            if ball_counter.get(entities[0]) < int(entities[1]):
                ball_counter[entities[0]] = int(entities[1])
    total = 1
    for counter in ball_counter.values():
        total = total * counter
    return total

def read_input(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

lines = read_input("input.txt")
total = sum( check_minimum_balls(line) for line in lines)
print(total)

