
# find all possible combinations of ball to be drawn
# from 12 red cubes, 13 green cubes, and 14 blue cubes
# store each of them in a list of objects.


# import and clean the input data
games = []
with open('./day_2/input.txt') as file:
    for line in file:
        game = {
            'game':int(line.split(':')[0].split(' ')[-1].strip()),
            'draws':[]
            }
        game_possibility = True
        config = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for draw in line.split(':')[1].split(';'):
            draw_object = {}
            for color_draw in draw.split(','):
                       color = color_draw.strip().split(' ')[1]
                       color_value = int(color_draw.strip().split(' ')[0])
                       if color_value>config[color]:
                             config[color] = color_value
                       draw_object[color] = color_value

            game['draws'].append(draw_object)
        product = 1
        for color in config.keys():
              product*=config[color]
        game['power'] = product
        games.append(game)


power_of_games = [game['power'] for game in games]
print(sum(power_of_games))
