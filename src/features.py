import numpy as np
import pandas as pd

def build_game_outcomes(pbp: pd.DataFrame) -> pd.DataFrame:
    g = pbp.groupby("game_id", as_index=False).agg(
        home_team=("home_team", "first"),
        away_team=("away_team", "first"),
        home_score=("home_score", "max"),
        away_score=("away_score", "max"),
    )
    g["home_win"] = (g["home_score"] > g["away_score"]).astype(int)
    return g

def attach_home_win_label(pbp, outcomes):
    return pbp.merge(outcomes[["game_id", "home_win"]], on="game_id", how="left")

def make_wp_features(df):
    df = df.copy()
    df["is_home_possession"] = (df["posteam"] == df["home_team"]).astype(int)
    df["score_diff_home"] = df["home_score"].fillna(0) - df["away_score"].fillna(0)
    df["time_remaining"] = df["game_seconds_remaining"].clip(lower=0)
    df["ydstogo"] = df["ydstogo"].clip(0, 50)
    df["yardline_100"] = df["yardline_100"].clip(1, 99)
    return df

def select_model_rows(df):
    return df[
        df["down"].isin([1,2,3,4]) &
        df["ydstogo"].notna() &
        df["yardline_100"].notna() &
        df["home_win"].notna()
    ]
