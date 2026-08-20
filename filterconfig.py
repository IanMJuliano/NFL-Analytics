#filter_config contains allowed data types for the play filter. Team, Week, and side of ball are also parameters that are already included.

filter_config = {
    "play_type": {
        "column": "play_type",
        "type": "exact"
    },

    "down": {
        "column": "down",
        "type": "exact"
    },

    "quarter": {
        "column": "qtr",
        "type": "exact"
    },

    "pass_length": {
        "column": "pass_length",
        "type": "exact"
    },
    "touchdown": {
        "column": "touchdown",
        "type": "exact"
    },
    "yards_gained": {
        "column": "yards_gained",
        "type": "range"
    }


}


stat_config = {
    "Yards per play": {
        "column": "yards_gained",
        "format": "number",
        "operation": "mean",
        "group": "Efficiency"
    },
    "EPA per play": {
        "column": "epa",
        "format": "number",
        "operation": "mean",
        "group": "Efficiency"
    },
    "Success rate": {
        "column": "success",
        "format": "percent",
        "operation": "mean",
        "group": "Efficiency"
    },
    "First down rate": {
        "column": "first_down",
        "format": "percent",
        "operation": "mean",
        "group": "Efficiency"
    },
    "Touchdown rate": {
        "column": "touchdown",
        "format": "percent",
        "operation": "mean",
        "group": "Efficiency"
    },
    "Total Yards": {
        "column": "yards_gained",
        "format": "number",
        "operation": "sum",
        "group": "Volume"
    },
    "Total Touchdowns": {
        "column": "touchdown",
        "format": "number",
        "operation": "sum",
        "group": "Volume"
    }
}
