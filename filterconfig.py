#filter_config contains allowed data types for the play filter. Team, Week, and side of ball are also parameters that are already included.

filter_config = {

    "home_team": {
        "column": "home_team",
        "type": "exact"
    },

    "away_team": {
        "column": "away_team",
        "type": "exact"
    },

    "play_type": {
        "column": "play_type",
        "type": "exact"
    },

    "down": {
        "column": "down",
        "type": "range"
    },

    "quarter": {
        "column": "qtr",
        "type": "exact"
    },

    "shotgun": {
        "column": "shotgun",
        "type": "exact"
    },

    "no_huddle": {
        "column": "no_huddle",
        "type": "exact"
    },

    "pass_length": {
        "column": "pass_length",
        "type": "exact"
    },

    "pass_location": {
        "column": "pass_location",
        "type": "exact"
    },

    "run_location": {
        "column": "run_location",
        "type": "exact"
    },

    "run_gap": {
        "column": "run_gap",
        "type": "exact"
    },

    "touchdown": {
        "column": "touchdown",
        "type": "exact"
    },

    "yards_gained": {
        "column": "yards_gained",
        "type": "range"
    },

    "epa": {
        "column": "epa",
        "type": "range"
    },

    "yards_to_go": {
        "column": "ydstogo",
        "type": "range"
    },

    "yardline_100": {
        "column": "yardline_100",
        "type": "range"
    },

    "game_seconds_remaining": {
        "column": "game_seconds_remaining",
        "type": "range"
    },

    "half_seconds_remaining": {
        "column": "half_seconds_remaining",
        "type": "range"
    },

    "quarter_seconds_remaining": {
        "column": "quarter_seconds_remaining",
        "type": "range"
    },

    "score_differential": {
        "column": "score_differential",
        "type": "range"
    },

    "goal_to_go": {
        "column": "goal_to_go",
        "type": "exact"
    },

    "first_down": {
        "column": "first_down",
        "type": "exact"
    },

    "qb_dropback": {
        "column": "qb_dropback",
        "type": "exact"
    },

    "qb_scramble": {
        "column": "qb_scramble",
        "type": "exact"
    },

    "pass_attempt": {
        "column": "pass_attempt",
        "type": "exact"
    },

    "rush_attempt": {
        "column": "rush_attempt",
        "type": "exact"
    },

    "complete_pass": {
        "column": "complete_pass",
        "type": "exact"
    },

    "incomplete_pass": {
        "column": "incomplete_pass",
        "type": "exact"
    },

    "interception": {
        "column": "interception",
        "type": "exact"
    },

    "fumble_lost": {
        "column": "fumble_lost",
        "type": "exact"
    },

    "sack": {
        "column": "sack",
        "type": "exact"
    },

    "air_yards": {
        "column": "air_yards",
        "type": "range"
    },

    "yards_after_catch": {
        "column": "yards_after_catch",
        "type": "range"
    },

    "cpoe": {
        "column": "cpoe",
        "type": "range"
    },

    "passer_player_name": {
        "column": "passer_player_name",
        "type": "exact"
    },

    "rusher_player_name": {
        "column": "rusher_player_name",
        "type": "exact"
    },

    "receiver_player_name": {
        "column": "receiver_player_name",
        "type": "exact"
    }
}