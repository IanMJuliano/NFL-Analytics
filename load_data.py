import nflreadpy as nfl

pbp = nfl.load_pbp([2025])

#README
    #The Parameters of def get_plays() are the allowed data types. 
    #All Yes or No datatypes use 1.0 or 0.0

def get_plays(team, 
                week, 
                side=None, 
                down=None, 
                quarter=None,
                play_type=None,
                pass_length = None,
                yards_gained = None,
                touchdown = None):
    game = game_one_side(team, week, side)

    filter_values = {
        "play_type": play_type,
        "down": down,
        "qtr": quarter,
        "pass_length": pass_length,
        "yards_gained": yards_gained,
        "touchdown": touchdown
    }

    correct_values = True
    for column, value in filter_values.items():

        if value is None: 
            continue

        allowed = get_allowed_data_entries(column)

        if value not in allowed:
            print(f"Invalid value ({value}) entered for data type: ({column}) ... Allowed values are {allowed}")
            correct_values = False
            continue
        
        game = game.filter(
            game[column] == value
        )

    if correct_values == False: 
        return "please try again!"
    else:
        return game

def get_allowed_data_entries(data_type):
    series = pbp.get_column(data_type)

    return (
        series
        .drop_nulls()
        .unique()
        .sort()
        .to_list()
    )

def full_game(
            team,
            week,) :
    game = pbp.filter(
        (pbp["week"] == week) &
        (
            (pbp["home_team"] == team) |
            (pbp["away_team"] == team)
        )
    )

    if game.is_empty():
        print("Bye Week")
        return game

    home_team = game["home_team"][0]
    away_team = game["away_team"][0]

    opponent = away_team if team == home_team else home_team

    print(f"{team} vs {opponent} - Week {week}")
    return game

def game_one_side(team, week, side):
    game = full_game(team, week)

    if side == "offense":
        return game.filter(
            game["posteam"] == team
        )
    elif side == "defense":
        return game.filter(
            game["defteam"] == team
        )
    else: 
        print("incorrect entry for side, please enter offense or defense.") 
        return game

def summarize_plays(plays_sheet): 
    stats = {
        "Yards per play": {
            "column": "yards_gained",
            "format": "number",
            "operation": "mean"
        },
        "EPA per play": {
            "column": "epa",
            "format": "number",
            "operation": "mean"
        },
        "Success rate": {
            "column": "success",
            "format": "percent",
            "operation": "mean"
        },
        "First down rate": {
            "column": "first_down",
            "format": "percent",
            "operation": "mean"
        },
        "Touchdown rate": {
            "column": "touchdown",
            "format": "percent",
            "operation": "mean"
        },
        "Total Yards": {
            "column": "yards_gained",
            "format": "number",
            "operation": "sum"
        },

        "Total Touchdowns": {
            "column": "touchdown",
            "format": "number",
            "operation": "sum"
        },
    }

    stat_organization: list[tuple[str, object]] = [
        ("Plays", len(plays_sheet))
    ]

    for stat_name, i in stats.items():

        column = i["column"]
        operation = i["operation"]
        format_type = i["format"]

        if operation == "mean":
            value = plays_sheet[column].mean()  
        elif operation == "sum":
            value = plays_sheet[column].sum()
        else:
            raise ValueError(f"Unknown operation - {operation}")

        if format_type == "percent":
            value = f"{value:.1%}"
        elif format_type == "number":
            value = round(value, 2)

        stat_organization.append(
            (stat_name, value)
        )    
    return stat_organization

def display_stats(stats, sort_method ="original"):
    if sort_method == "alphabetical":
        stats = sorted(stats, key=lambda stat: stat[0])

    for stat_name, value in stats:
        print(f"{stat_name:<20} {value}")
    
display_stats(summarize_plays(get_plays(team = "CAR", down = 1, week = 11, play_type = "pass", side = "offense", pass_length = "deep")), sort_method="alphabetical")