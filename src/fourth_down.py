import numpy as np
import pandas as pd

def label_decision(df):
    decision = pd.Series("other", index=df.index)

    if "punt_attempt" in df:
        decision[df["punt_attempt"] == True] = "punt"
    if "field_goal_attempt" in df:
        decision[df["field_goal_attempt"] == True] = "field_goal"

    go = (
        df.get("pass_attempt", False) |
        df.get("rush_attempt", False) |
        df["play_type"].isin(["run", "pass", "sack", "qb_kneel", "qb_spike"])
    )
    decision[(decision == "other") & go] = "go_for_it"
    return decision

def kick_distance_from_yardline100(y):
    return y + 17
