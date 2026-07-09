def total_goals(df):
    home_goals = df["HOME_TEAM_SCORE"].sum()
    away_goals = df["AWAY_TEAM_SCORE"].sum()

    total_goals = home_goals + away_goals
    average_goals = total_goals / df.shape[0]

    return total_goals, average_goals


def top_scoring_teams(df):
    home_goals = df.groupby("HOME_TEAM")["HOME_TEAM_SCORE"].sum()
    away_goals = df.groupby("AWAY_TEAM")["AWAY_TEAM_SCORE"].sum()

    total_goals_by_team = home_goals.add(away_goals, fill_value=0)
    total_goals_by_team = total_goals_by_team.sort_values(ascending=False)

    return total_goals_by_team


def top_conceded_teams(df):
    home_conceded = df.groupby("HOME_TEAM")["AWAY_TEAM_SCORE"].sum()
    away_conceded = df.groupby("AWAY_TEAM")["HOME_TEAM_SCORE"].sum()

    total_conceded = home_conceded.add(away_conceded, fill_value=0)
    total_conceded = total_conceded.sort_values(ascending=False)

    return total_conceded


def home_advantage(df):
    home_wins = (df["HOME_TEAM_SCORE"] > df["AWAY_TEAM_SCORE"]).sum()
    draws = (df["HOME_TEAM_SCORE"] == df["AWAY_TEAM_SCORE"]).sum()
    away_wins = (df["HOME_TEAM_SCORE"] < df["AWAY_TEAM_SCORE"]).sum()

    return home_wins, draws, away_wins

def average_attendance(df):
    average_attendance = df["ATTENDANCE"].mean()

    return average_attendance

def top_attendance_matches(df):
    top_matches = df.sort_values(
        by="ATTENDANCE",
        ascending=False
    ).head(10)

    return top_matches[
        ["HOME_TEAM", "AWAY_TEAM", "STADIUM", "ATTENDANCE"]
    ]

def goals_by_season(df):
    df["TOTAL_GOALS"] = df["HOME_TEAM_SCORE"] + df["AWAY_TEAM_SCORE"]

    goals = df.groupby("SEASON")["TOTAL_GOALS"].sum()

    return goals

def matches_by_season(df):
    return df.groupby("SEASON").size()

def average_goals_by_season(df):
    df["TOTAL_GOALS"] = df["HOME_TEAM_SCORE"] + df["AWAY_TEAM_SCORE"]

    goals = df.groupby("SEASON")["TOTAL_GOALS"].sum()
    matches = df.groupby("SEASON").size()

    average_goals = goals / matches

    return average_goals

def average_attendance_by_season(df):
    average_attendance = df.groupby("SEASON")["ATTENDANCE"].mean()

    return average_attendance

def average_height(df):
    return df["HEIGHT"].mean()

def tallest_players(df):
    tallest = df.sort_values(
        by="HEIGHT",
        ascending=False
    ).head(10)

    return tallest[
        ["FIRST_NAME", "LAST_NAME", "TEAM", "POSITION", "HEIGHT"]
    ]

def average_height_by_position(df):
    players = df[
        df["POSITION"].isin([
            "Goalkeeper",
            "Defender",
            "Midfielder",
            "Forward"
        ])
    ]

    return players.groupby("POSITION")["HEIGHT"].mean().sort_values(ascending=False)

import pandas as pd

def average_age(df):
    players = df[
        df["POSITION"].isin([
            "Goalkeeper",
            "Defender",
            "Midfielder",
            "Forward"
        ])
    ].copy()

    players["DOB"] = pd.to_datetime(players["DOB"])
    players["AGE"] = 2026 - players["DOB"].dt.year

    return players["AGE"].mean()

def average_age_by_position(df):
    players = df[
        df["POSITION"].isin([
            "Goalkeeper",
            "Defender",
            "Midfielder",
            "Forward"
        ])
    ].copy()

    players["DOB"] = pd.to_datetime(players["DOB"])
    players["AGE"] = 2026 - players["DOB"].dt.year

    return players.groupby("POSITION")["AGE"].mean()