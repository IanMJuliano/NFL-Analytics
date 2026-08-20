stat_config = {
    "Yards per play": {
        "column": "yards_gained",
        "operation": "mean",
        "format": "number",
        "group": "Efficiency",
        "sides": ["offense", "defense"],
        "defense_name": "Yards allowed per play"
    },

    "EPA per play": {
        "column": "epa",
        "operation": "mean",
        "format": "number",
        "group": "Efficiency",
        "sides": ["offense", "defense"],
        "defense_name": "EPA allowed per play"
    },

    "Success rate": {
        "column": "success",
        "operation": "mean",
        "format": "percent",
        "group": "Efficiency",
        "sides": ["offense", "defense"],
        "defense_name": "Success rate allowed"
    },

    "First down rate": {
        "column": "first_down",
        "operation": "mean",
        "format": "percent",
        "group": "Efficiency",
        "sides": ["offense", "defense"],
        "defense_name": "First down rate allowed"
    },

    "Touchdown rate": {
        "column": "touchdown",
        "operation": "mean",
        "format": "percent",
        "group": "Efficiency",
        "sides": ["offense", "defense"],
        "defense_name": "Touchdown rate allowed"
    },

    "Average air yards": {
        "column": "air_yards",
        "operation": "mean",
        "format": "number",
        "group": "Efficiency",
        "sides": ["offense", "defense"],
        "defense_name": "Average air yards allowed",
        "play_type": "pass"
    },

    "Average yards after catch": {
        "column": "yards_after_catch",
        "operation": "mean",
        "format": "number",
        "group": "Efficiency",
        "sides": ["offense", "defense"],
        "defense_name": "Average YAC allowed",
        "play_type": "pass"
    },

    "CPOE": {
        "column": "cpoe",
        "operation": "mean",
        "format": "number",
        "group": "Efficiency",
        "sides": ["offense", "defense"],
        "defense_name": "Opponent CPOE",
        "play_type": "pass"
    },

    "Fumble lost rate": {
        "column": "fumble_lost",
        "operation": "mean",
        "format": "percent",
        "group": "Efficiency",
        "sides": ["offense", "defense"],
        "defense_name": "Opponent fumble lost rate"
    },

    "Total yards": {
        "column": "yards_gained",
        "operation": "sum",
        "format": "number",
        "group": "Volume",
        "sides": ["offense", "defense"],
        "defense_name": "Total yards allowed"
    },

    "Total touchdowns": {
        "column": "touchdown",
        "operation": "sum",
        "format": "number",
        "group": "Volume",
        "sides": ["offense", "defense"],
        "defense_name": "Touchdowns allowed"
    },

    "Total EPA": {
        "column": "epa",
        "operation": "sum",
        "format": "number",
        "group": "Volume",
        "sides": ["offense", "defense"],
        "defense_name": "Total EPA allowed"
    },

    "Successful plays": {
        "column": "success",
        "operation": "sum",
        "format": "number",
        "group": "Volume",
        "sides": ["offense", "defense"],
        "defense_name": "Successful plays allowed"
    },

    "First downs": {
        "column": "first_down",
        "operation": "sum",
        "format": "number",
        "group": "Volume",
        "sides": ["offense", "defense"],
        "defense_name": "First downs allowed"
    },

    "Pass attempts": {
        "column": "pass_attempt",
        "operation": "sum",
        "format": "number",
        "group": "Volume",
        "sides": ["offense", "defense"],
        "defense_name": "Pass attempts faced",
        "play_type": "pass"
    },

    "Rush attempts": {
        "column": "rush_attempt",
        "operation": "sum",
        "format": "number",
        "group": "Volume",
        "sides": ["offense", "defense"],
        "defense_name": "Rush attempts faced",
        "play_type": "run"
    },

    "Completions": {
        "column": "complete_pass",
        "operation": "sum",
        "format": "number",
        "group": "Volume",
        "sides": ["offense", "defense"],
        "defense_name": "Completions allowed",
        "play_type": "pass"
    },

    "Interceptions": {
        "column": "interception",
        "operation": "sum",
        "format": "number",
        "group": "Volume",
        "sides": ["offense", "defense"],
        "defense_name": "Interceptions forced",
        "play_type": "pass"
    },

    "Fumbles lost": {
        "column": "fumble_lost",
        "operation": "sum",
        "format": "number",
        "group": "Volume",
        "sides": ["offense", "defense"],
        "defense_name": "Opponent fumbles lost"
    },

    "Sacks Taken": {
        "column": "sack",
        "operation": "sum",
        "format": "number",
        "group": "Volume",
        "sides": ["offense", "defense"],
        "defense_name": "Sacks generated",
        "play_type": "pass"
    },

    "Total air yards": {
        "column": "air_yards",
        "operation": "sum",
        "format": "number",
        "group": "Volume",
        "sides": ["offense", "defense"],
        "defense_name": "Total air yards allowed",
        "play_type": "pass"
    },

    "Total YAC": {
        "column": "yards_after_catch",
        "operation": "sum",
        "format": "number",
        "group": "Volume",
        "sides": ["offense", "defense"],
        "defense_name": "Total YAC allowed",
        "play_type": "pass"
    },

    "Completion percentage": {
        "operation": "ratio",
        "numerator": "complete_pass",
        "denominator": "pass_attempt",
        "format": "percent",
        "group": "Efficiency",
        "sides": ["offense", "defense"],
        "defense_name": "Completion percentage allowed",
        "play_type": "pass"
    }
}