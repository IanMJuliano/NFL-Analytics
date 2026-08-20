import nflreadpy as nfl
pbp = nfl.load_pbp([2025])

from filterconfig import filter_config
from statconfig import stat_config

#README
    #The Parameters of def get_plays() are the allowed data types. 
    #All Yes or No datatypes use 1.0 or 0.0

def get_plays(team, 
                week, 
                side=None,
                **kwargs):
    game = get_game(team, week, side)

    for filter_name, value in kwargs.items():
        if filter_name not in filter_config:
            raise ValueError(f"Invalid filter: {filter_name}")

        config = filter_config[filter_name]
        column = config["column"]
        filter_type = config["type"]

        if value is None:
            continue

        if filter_type == "exact":
            allowed = get_allowed_data_entries(column)

            if value not in allowed:
                raise ValueError(
                    f"Invalid value ({value}) entered for data type: "
                    f"({column}) ... Allowed values are {allowed}"
                )

            game = game.filter(
                game[column] == value
            )
        elif filter_type == "range":

            if not isinstance(value, tuple) or len(value) != 2:
                raise ValueError(f"{filter_name} must be entered as (min, max)")

            minimum, maximum = value
            if not isinstance(minimum, (int, float)) or not isinstance(maximum, (int, float)):
                raise ValueError(f"{filter_name} range values must be numbers.")

            if minimum > maximum:
                raise ValueError(f"{filter_name} minimum cannot be greater than maximum.")

            series = game.get_column(column)
            game = game.filter(
                (series >= minimum) &
                (series <= maximum)
            )
        else:
            raise ValueError(f"Unknown filter type - {filter_type}")
    return game, team, week, side, kwargs

def get_allowed_data_entries(data_type):
    series = pbp.get_column(data_type)

    return (
        series
        .drop_nulls()
        .unique()
        .sort()
        .to_list()
    )

def get_game(team,week, side=None):

    if isinstance(week, int):
        weeks = [week]
    elif isinstance (week, tuple):
        weeks = list(week)
    else:
        raise ValueError("Please enter week value 1-17 as 1 or (1, x) or enter 0 for the entire season")

    if week != 0:
        game = pbp.filter(
            pbp["week"].is_in(weeks) &
            (
                    (pbp["home_team"] == team) |
                    (pbp["away_team"] == team)
            )
        )
    else:
        game = pbp.filter(
            (pbp["home_team"] == team) |
            (pbp["away_team"] == team)
        )

    if side == "offense":
        game = game.filter(
            game["posteam"] == team
        )
    elif side == "defense":
        game = game.filter(
            game["defteam"] == team
        )
    elif side is not None:
        raise ValueError("incorrect entry for side, please enter offense or defense.")

    return game

def summarize_plays(result):
    plays_sheet, team, week, side, filters = result


    if plays_sheet.is_empty():
        return [("Plays", 0, "Volume")], team, week, side

    stat_organization: list[tuple[str, object, str]] = [
        ("Plays", len(plays_sheet), "Volume")
    ]

    selected_play_type = filters.get("play_type")

    for stat_name, i in stat_config.items():
        allowed_side = i.get("sides")
        required_play_type = i.get("play_type")

        if allowed_side is not None and side is not None and side not in allowed_side != side:
            continue
        if required_play_type is not None and selected_play_type is not None and required_play_type != selected_play_type:
            continue

        display_name = stat_name
        if side == "defense":
            display_name = i.get("defense_name", stat_name)

        operation = i["operation"]
        format_type = i["format"]
        group = i["group"]

        value = None
        if operation == "ratio":
            numerator = plays_sheet[i["numerator"]].sum()
            denominator = plays_sheet[i["denominator"]].sum()

            if denominator is not None and denominator != 0 and numerator is not None:
                value = float(numerator) / float(denominator)

        elif operation in ("mean", "sum"):
            column = i["column"]
            if operation == "mean":
                value = plays_sheet[column].mean()
            elif operation == "sum":
                value = plays_sheet[column].sum()
        else:
            raise ValueError(f"Unknown operation - {operation}")

        if value is None:
            value = "N/A"
        elif format_type == "percent":
            value = f"{float(value):.1%}"
        elif format_type == "number":
            value = round(float(value), 2)

        stat_organization.append(
            (display_name, value, group)
        )    
    return stat_organization, team, week, side

#Sort methods, Alphabetical & Original
#Grouping by group type
def display_stats(result, sort_method ="original", group =False):
    stats, team, week, side = result

    if week == 0:
        print(f"{team} - Full Season")
    elif isinstance(week, int):
            print(f"{team} Week {week}")
    else:
        week_text = ", ".join(map(str, week))
        print(f"\n{team} - Weeks {week_text}")

    if sort_method == "alphabetical":
        stats = sorted(stats, key=lambda stat: stat[0])
    if group:
        groups = {}
        for stat_name, value, group_name in stats:
            if group_name not in groups:
                groups[group_name] = []
            groups[group_name].append(
                (stat_name, value)
            )
        for group_name, group_stats in groups.items():
            print(f"\n-- {group_name} --")

            for stat_name, value in group_stats:
                print(f"{stat_name:<20} {value}")
    else:
        for stat_name, value, group_name in stats:
            print(f"{stat_name:<20} {value}")

display_stats(summarize_plays(get_plays(team = "CAR",
                                        down = (1, 4),
                                        week = 0,
                                        play_type = "pass",
                                        side = "defense",
                                        yards_to_go = (0, 50),
                                        shotgun = 0,
                                        yards_gained = (0, 20),
                                        score_differential = (0, 20))),

                                                sort_method="alphabetical",
                                                group=True)