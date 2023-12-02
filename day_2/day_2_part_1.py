
# find all possible combinations of ball to be drawn
# from 12 red cubes, 13 green cubes, and 14 blue cubes
# store each of them in a list of objects.
config = {
    'red': 12,
    'green': 13,
    'blue': 14
}

# import and clean the input data
games = []
with open('./day_2/input.txt') as file:
    for line in file:
        game = {
            'game':int(line.split(':')[0].split(' ')[-1].strip()),
            'draws':[]
            }
        game_possibility = True
        for draw in line.split(':')[1].split(';'):
            draw_object = {}
            for color_draw in draw.split(','):
                       color = color_draw.strip().split(' ')[1]
                       color_value = int(color_draw.strip().split(' ')[0])
                       if color_value>config[color]:
                             game_possibility = False
                       draw_object[color] = color_value
            for color in config.keys():
                 if color not in draw_object.keys():
                      draw_object[color]: 0
            game['draws'].append(draw_object)
        game['game_possibility'] = game_possibility
        games.append(game)

# check if each draw exists in the possible combinations
# save the game id in a list of possible games
possible_games = [game['game'] for game in games if game['game_possibility']]
print(sum(possible_games))
