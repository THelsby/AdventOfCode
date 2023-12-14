ball_limit = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
}

def read_input(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def validate_game(game):
    game = game.split(':')
    rounds = game[1].split(';')
    for round in rounds:
        events = round.split(',')
        for event in events:
            entities = event.split()[::-1]
            if ball_limit.get(entities[0]) < int(entities[1]):
                return 0
    return int(game[0].split()[1])


lines = read_input("input.txt")
total = sum(validate_game(line) for line in lines)

print(total)